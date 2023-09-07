# -*- coding: utf-8 -*-

"""
    :mod:`dbsettings`
    ===========================================================================
    :synopsis: default data and constants for the database
    :author: Roberto Magán Carrión
    :contact: roberto.magan@uca.es, rmagan@ugr.es, robertomagan@gmail.com
    :organization: University of Cádiz, University of Granada
    :project: I2P Crawler
    :since: 0.0.1
"""

from enum import Enum, unique

# Site status and type constants
# SITE STATUS

@unique
class Status(Enum):
    ONGOING = 1
    FINISHED = 2
    PENDING = 3
    ERROR = 4
    DISCARDED = 5
    DISCOVERING = 6
    ERROR_DEFUNC = 7
    PRE_DISCOVERING = 8


# {status:description}
SITE_STATUS_DEFAULT_INFO = {Status.ONGOING.name: 'Ongoing: The site is being crawled',
                            Status.FINISHED.name: 'Finished: The site has been successfully crawled',
                            Status.PENDING.name: 'Pending: The site is waiting to be launched again.'
                                                ' May there was a processing error.',
                            Status.ERROR.name: 'Error: The site cannot be crawled',
                            Status.DISCARDED.name: 'Discarded: The site  has been discarded because the '
                                                   'number of maximum tries or the temporal window is expired.',
                            Status.DISCOVERING.name: 'Discovering: The site is being discovered.',
                            Status.PRE_DISCOVERING.name: 'Pre-discovering: a seed site which is waiting to '
                                                         'be assigned to a specific manager.',
                            Status.ERROR_DEFUNC.name: 'The spider subprocess has been stopped by the S.O.'}

# SITE TYPE
@unique
class Type(Enum):
    I2P = 1
    TOR = 2
    SURFACE = 3
    UNKNOWN = 4
    FREENET = 5


#{type:description}
SITE_TYPE_DEFAULT_INFO = {Type.I2P.name: 'I2P eepsite',
                          Type.TOR.name: 'TOR onion site',
                          Type.SURFACE.name: 'Surface web site',
                          Type.UNKNOWN.name: 'Unknown site type',
                          Type.FREENET.name: 'Freenet freesite'}


# SITE SOURCE
@unique
class Source(Enum):
    SEED = 1
    FLOODFILL = 2
    DISCOVERED = 3
    UNKNOWN = 4


#{source:description}
SITE_SOURCE_DEFAULT_INFO = {Source.SEED.name: 'Site got from initial seeds',
                            Source.FLOODFILL.name: 'Site got from a floodfill router.',
                            Source.DISCOVERED.name: 'Site discovered from a crawling process.',
                            Source.UNKNOWN.name: 'Unknown source.'}

