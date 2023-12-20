# -*- coding: utf-8 -*-

"""
    :mod:`settings`
    ===========================================================================
    :synopsis: crawling process configuration parameters
    :author: Roberto Magán Carrión
    :contact: roberto.magan@uca.es, rmagan@ugr.es, robertomagan@gmail.com
    :organization: University of Cádiz, University of Granada
    :project: I2P Crawler
    :since: 0.0.1
"""

# Config params
# Number of simultaneous spiders running
MAX_ONGOING_SPIDERS = 10
# Number of tries for error sites
MAX_CRAWLING_ATTEMPTS_ON_ERROR = 2
# Number of tries for error sites
MAX_CRAWLING_ATTEMPTS_ON_DISCOVERING = 1*24*14 # 14 days, 1 try per hour
# Number of tries for error sites
MAX_DURATION_ON_DISCOVERING = 24*14*60  # Minutes --> 14 days
# Number of parallel single threads running
MAX_SINGLE_THREADS_ON_DISCOVERING = 25
# Http response timeout
HTTP_TIMEOUT = 180  # Seconds
# Initial seed file
INITIAL_SEEDS = "seed_urls.txt"
# Batch size of initial seeds
INITIAL_SEEDS_BACH_SIZE = 60  # 592/10=59'2 = 60
# Time to wait until the next seeds self-assignment
SEEDS_ASSIGNMENT_PERIOD = 1200  # seconds (10 machine, 2 minute/machine --> 20 minutes )
# To schedule the discovering time. Each site will be discover every TIME_INTERVAL_TO_DISCOVER
TIME_INTERVAL_TO_DISCOVER = 60  # minutes