# -*- coding: utf-8 -*-

"""
    :mod:`discoverythread`
    ===========================================================================
    :synopsis: Thread for checking darksites availability
    :author: Roberto Magán Carrión
    :contact: roberto.magan@uca.es, rmagan@ugr.es, robertomagan@gmail.com
    :organization: University of Cádiz, University of Granada
    :project: I2P Crawler
    :since: 0.0.1
"""

import logging
import time
import threading
from datetime import datetime
from datetime import timedelta

import regex
from database import dbutils, dbsettings, entities, connection_settings
from pony.orm import db_session
from utils import siteutils

from .darknetthread import DarknetThread
from .qos import request_conn

# Set to True to show pony SQL queries
#set_sql_debug(debug=True)
# Regular expression for HTTP successful response codes
HTTP_SUCCES_COD_REGEXPR = '[23]'
reg_http = regex.compile(HTTP_SUCCES_COD_REGEXPR)


class DiscoveringThread(DarknetThread, object):

    def __init__(self, max_tries, duration, max_single_threads, http_request_timeout, uuid):
        super(DiscoveringThread, self).__init__()
        self._sites_to_discover = []
        self._max_tries = max_tries
        self._duration = duration
        self._max_single_threads = max_single_threads
        self._http_request_timeout = http_request_timeout
        self._uuid = uuid

    def run(self):

        # Doing until stop request
        while not self._stopped_event.isSet():

            with db_session:
                # Restoring the crawling status
                status = siteutils.get_crawling_status(self._uuid)
                # restored discovering sites
                self._sites_to_discover = status[dbsettings.Status.DISCOVERING.name]
                logging.debug("Current # of sites to discover %s.", len(self._sites_to_discover))

            # Running Threads
            simple_threads = []
            #running_threads = 0

            # While there are sites to discover and running threads
            while self._sites_to_discover or len(simple_threads) != 0:

                # How many simultaneous single threads are allowed to be running?
                while (self._max_single_threads - len(simple_threads)) > 0:
                    if self._sites_to_discover:
                        darksite = self._sites_to_discover.pop()
                        ssdThread = SingleSiteDiscoveryThread(self._max_tries, self._duration,
                                                              self._http_request_timeout, darksite)
                        ssdThread.setName("SingleSiteDiscoveryThread_"+str(darksite))
                        ssdThread.start()
                        #logging.debug("Running threads counter: %s",running_threads)
                        simple_threads.append(ssdThread)
                        #logging.debug("Simple threads: %s", [t.getName() if t is not None else None for t in simple_threads])
                        #running_threads += 1
                        logging.debug("Running %s", ssdThread.getName())
                    else:
                        break

                # Checking running threads
                for i, thread in enumerate(simple_threads):
                    if not thread.isAlive(): # if dead
                        del simple_threads[i]
                        #running_threads -= 1

                logging.debug("%s SingleSiteDiscoveryThread are running", len(simple_threads))
                logging.debug("There are %s sites to discover.", len(self._sites_to_discover))

                time.sleep(1)

            time.sleep(1)

    def on_stop(self):
        # Should be overridden to do some stuff on thread stop
        logging.debug("Stopping DiscoveryThread ...")


class SingleSiteDiscoveryThread(DarknetThread, object):

    def __init__(self, max_tries, duration, http_request_timeout, darksite):
        super(SingleSiteDiscoveryThread, self).__init__()
        self._max_tries = max_tries
        self._duration = duration
        self._http_request_timeout = http_request_timeout
        self._darksite = darksite

    def run(self):

            try:
                with db_session:
                    # Get next site
                    # darksite = self._sites_to_discover.pop()

                    logging.debug("Trying to discover site %s", self._darksite)

                    proc_log = dbutils.get_processing_logs_by_site_status(s_url=self._darksite,
                                                                          s_status=dbsettings.Status.DISCOVERING)
                    # Computes the time spent from the first discovering status of the darksite
                    time_spent = datetime.now() - proc_log[0].timestamp
                    # Do I reach schedule time to start the discovering process?
                    time_to_next_try = proc_log[-1].next_time_to_try - datetime.now()

                    discovering_tries = dbutils.get_site(s_url=self._darksite).discovering_tries

                    logging.debug("Time spent for site %s: %s ", self._darksite, time_spent)
                    logging.debug("Next discovering try for site %s: %s. Time to it: %s", self._darksite,
                                  proc_log[-1].next_time_to_try, time_to_next_try)
                    logging.debug("Current tries for site %s: %s ", self._darksite, discovering_tries)

                    if time_to_next_try <= timedelta(minutes=0):
                        # Checking maximum discovering tries and period of time for trying
                        if discovering_tries < self._max_tries \
                                and time_spent <= timedelta(minutes=self._duration):

                            darksite_http = "http://" + self._darksite
                            logging.debug("DISCOVERING: %s", self._darksite)
                            if not connection_settings.PROXY:
                                response = request_conn.connectThroughProxy(darksite_http,
                                                                        proxies=None,
                                                                        timeout=self._http_request_timeout)
                            else:
                                response = request_conn.connectThroughProxy(darksite_http,
                                                                        proxies={'http': 'http://'+connection_settings.PROXY},
                                                                        timeout=self._http_request_timeout)

                            response_code = str(response.status_code)
                            response_time = str(response.elapsed.total_seconds())
                            # Print CSV Line
                            csv_line = ""
                            csv_line += self._darksite + "|" + response_code + "|"
                            csv_line += response_time + "|" + str(discovering_tries)
                            logging.debug("RESPONSE: %s", csv_line)

                            logging.debug("Increasing discovering tries to site %s.", self._darksite)
                            dbutils.increase_tries_on_discovering(s_url=self._darksite)

                            # HTTP 2XX or 3XX
                            if reg_http.match(response_code):
                                dbutils.set_site_current_processing_status(s_url=self._darksite,
                                                                           s_http_status=response_code,
                                                                           s_http_response_time=response_time,
                                                                           s_status=dbsettings.Status.PENDING)
                                logging.debug("Site %s was set up to PENDING.", self._darksite)
                            # HTTP 4XX or 5XX
                            else:
                                dbutils.set_site_current_processing_status(s_url=self._darksite,
                                                                           s_http_status=response_code,
                                                                           s_http_response_time=response_time,
                                                                           s_status=dbsettings.Status.DISCOVERING)
                                logging.debug("Site %s was set up to DISCOVERING the response code %s received.", self._darksite, response_code)
                        else:
                            dbutils.set_site_current_processing_status(s_url=self._darksite,
                                                                       s_status=dbsettings.Status.DISCARDED)
                            logging.debug("Site %s was set up to DISCARDED because tries were %s (max %s) "
                                          "or duration was %s (max %s mins).", self._darksite, discovering_tries,
                                          self._max_tries, time_spent, self._duration)
                    else:
                        logging.debug("Site %s is not ready to be discover until %s. Time to it: %s", self._darksite,
                                      proc_log[0].next_time_to_try, time_to_next_try)

            except Exception as e:
                logging.error("ERROR on discovering %s: %s", self._darksite, e)
                logging.exception("ERROR:")
                logging.debug("Increasing discovering tries to site %s.", self._darksite)
                with db_session:
                    dbutils.increase_tries_on_discovering(s_url=self._darksite)
                    dbutils.set_site_current_processing_status(s_url=self._darksite,
                                                               s_http_status='',
                                                               s_http_response_time='',
                                                               s_status=dbsettings.Status.DISCOVERING)
                logging.debug("Site %s was set up to DISCOVERING because there was an HTTP error.", self._darksite)

    def on_stop(self):
        # Should be overridden to do some stuff on thread stop
        logging.debug("Stopping SingleSiteDiscoveryThread for site %s ",self._darksite )
