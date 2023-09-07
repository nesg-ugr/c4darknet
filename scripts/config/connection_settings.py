# -*- coding: utf-8 -*-

"""
    :mod:`connection_settings`
    ===========================================================================
    :synopsis: Settings about connection database and proxy
    :author: Emilio Figueras Martín
    :contact: emilio.figuerasmartin@alum.uca.es
    :organization: University of Cádiz
    :project: I2P Crawler
    :since: 0.0.1
"""

# Config db params
#Service of database
PROVIDER = 'mysql'

#DB host
HOST = '192.168.44.9'

#DB username
USERNAME = 'freenet'

#DB password
PASSWORD = '1Uchn53d'

#DB name
DATABASE = 'freenet_database'

#Proxy configuration (host:port or None)
# I2P = 127.0.0.1:4444
# FREENET = None
#PROXY = '127.0.0.1:4444'
PROXY = None