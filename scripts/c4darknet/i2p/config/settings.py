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
MAX_CRAWLING_ATTEMPTS_ON_DISCOVERING = 2*24*7 # 2 tries per hour during 7 days
# Number of tries for error sites
MAX_DURATION_ON_DISCOVERING = 60*24*7  # Minutes --> 7 days
# Number of parallel single threads running
MAX_SINGLE_THREADS_ON_DISCOVERING = 25
# Http response timeout
HTTP_TIMEOUT = 180  # Seconds
# Initial seed file
INITIAL_SEEDS = "i2p_seeds.txt"
# Batch size of initial seeds
INITIAL_SEEDS_BACH_SIZE = 3162 # 6324/2=3162
# Time to wait until the next seeds self-assignment
SEEDS_ASSIGNMENT_PERIOD = 240  # seconds (2 machines, 2 minute/machine --> 4 minutes )
# To schedule the discovering time. Each site will be discover every TIME_INTERVAL_TO_DISCOVER
TIME_INTERVAL_TO_DISCOVER = 30  # minutes
