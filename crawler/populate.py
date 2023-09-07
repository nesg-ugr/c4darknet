# -*- coding: utf-8 -*-

"""
    :mod:`populate`
    ===========================================================================
    :synopsis: populates database tables and adds default info
    :author: Roberto Magán Carrión
    :contact: roberto.magan@uca.es, rmagan@ugr.es, robertomagan@gmail.com
    :organization: University of Cádiz, University of Granada
    :project: I2P Crawler
    :since: 0.0.1
"""

from pony.orm import sql_debug, db_session
from database import dbsettings
from database import entities
from database import dbutils
from utils import siteutils
from darknet import darknetsettings
import settings
import logging

sql_debug(True)


def add_default_info():
    """
    Adds default information to the database

    """
    with db_session:
        # Adding site types
        add_default_site_types()
    with db_session:
        # Adding site status
        add_default_site_status()
    with db_session:
        # Adding site sources
        add_default_site_sources()
    with db_session:
        # Adding pre-discovering seed sites
        add_prediscovering_sites()


def add_default_site_status():
    """
    Adds default status for site crawling.

    """
    for status in list(dbsettings.SITE_STATUS_DEFAULT_INFO.keys()):
        entities.SiteStatus(type=status, description=dbsettings.SITE_STATUS_DEFAULT_INFO[status])


def add_default_site_types():
    """
    Adds default types of sites found.

    """
    for type in list(dbsettings.SITE_TYPE_DEFAULT_INFO.keys()):
        entities.SiteType(type=type, description=dbsettings.SITE_TYPE_DEFAULT_INFO[type])


def add_default_site_sources():
    """
    Adds default sources of sites found.

    """
    for source in list(dbsettings.SITE_SOURCE_DEFAULT_INFO.keys()):
        entities.SiteSource(type=source, description=dbsettings.SITE_SOURCE_DEFAULT_INFO[source])


def add_prediscovering_sites():

    # Gets initial seeds
    seed_sites = siteutils.get_seeds_from_file(darknetsettings.PATH_DATA + settings.INITIAL_SEEDS)

    # Create all sites in DISCOVERING status. Note that if the site exists, it will not be created
    for site in seed_sites:
        site_type = siteutils.get_type_site(site)

        #if its a freesite, clear url
        if site_type.name is "FREENET":
            site = site.replace('https://', '')
            site = site.replace('http://', '')
            site = site.replace('freenet:', '')
            if site[-1] is '/':
                site = site[:-1]

        # is it a new site? Create it and set up the status to pending.
        if dbutils.create_site(s_url=site, s_type=site_type ,s_uuid=''):
            dbutils.set_site_current_processing_status(s_url=site, s_status=dbsettings.Status.PRE_DISCOVERING,
                                                       add_processing_log=False)


def add_fake_discovery_info():
    """
    Adds default discovery info just for testing dicovering procedure
    """

    valid_site = 'no.i2p'
    #dbutils.create_site(valid_site)
    #dbutils.set_site_current_processing_status(s_url=valid_site, s_status=dbsettings.Status.DISCOVERING)

    not_valid_site = 'fake.i2p'
    dbutils.create_site(not_valid_site)
    dbutils.set_site_current_processing_status(s_url=not_valid_site, s_status=dbsettings.Status.DISCOVERING)

    not_valid_site_2 = 'fake_2.i2p'
    dbutils.create_site(not_valid_site_2)
    dbutils.set_site_current_processing_status(s_url=not_valid_site_2, s_status=dbsettings.Status.DISCOVERING)

    not_valid_site_3 = 'fake_3.i2p'
    dbutils.create_site(not_valid_site_3)
    dbutils.set_site_current_processing_status(s_url=not_valid_site_3, s_status=dbsettings.Status.DISCOVERING)

    # Simulates the discovering process
    # Valid site
    # Discovering process of valid site got 2xx o 3xx http status
    #dbutils.set_site_current_processing_status(s_url=valid_site, s_status=dbsettings.Status.DISCOVERING,
    #                                           s_http_status='200')

    # Fake site
    # Discovering process of fake site got 4xx o 5xx http status
    #dbutils.set_site_current_processing_status(s_url=not_valid_site, s_status=dbsettings.Status.DISCOVERING,
    #                                           s_http_status='500')


def add_default_languages():
    #TODO populate all languages
    pass

def main():
    """
    Creates the schema and adds initial default info.

    """

    add_default_info()
    #add_fake_discovery_info()

if __name__ == '__main__':
    main()