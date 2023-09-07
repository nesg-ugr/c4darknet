# -*- coding: utf-8 -*-


"""
    :mod:`siteutils`
    ===========================================================================
    :synopsis: site utilities
    :author: Roberto Magán Carrión
    :contact: roberto.magan@uca.es, rmagan@ugr.es, robertomagan@gmail.com
    :organization: University of Cádiz, University of Granada
    :project: I2P Crawler
    :since: 0.0.1
"""

from pony.orm import db_session

from database import dbutils, dbsettings

import os
import logging
import uuid
import re


def get_seeds_from_file(path_to_file):
    """
    Gets a list of initial site seeds

    :param path_to_file: srt - Path to the *.txt file of gathered site seeds
    :return: new_list: list - Site seed list
    """

    # New list
    new_list = []

    try:
        # Gets all seeds from the file
        with open(path_to_file) as seeds:
            list_seeds = seeds.readlines()

        # Postprocessing the list
        for seed in list_seeds:
            seed = str.replace(seed, '\n', '')
            seed = str.replace(seed, '\r', '')
            new_list.append(seed)

    except Exception as e:
        logging.debug("ERROR getting seeds: %s", e)

    return new_list


def tail(path_to_file, n=1):
    """
    Executes tail on unix based systems

    :param path_to_file: str - Path to the file
    :param n: int - Number of lines
    :return: lines_str: str - Last n lines concatenated
    """

    lines_str = os.popen('tail -n ' + str(n) + ' ' + path_to_file).read()
    return lines_str


def get_crawling_status(uuid):
    """
    Gets a snapshot of how the crawling procedure is going

    :param uuid: str - Crawling process UUID
    :return: status: dict - The current crawling status
    """

    status = {}

    with db_session:
        status[dbsettings.Status.PENDING.name] = \
            dbutils.get_sites_names_by_processing_status(s_status=dbsettings.Status.PENDING, uuid=uuid, sorting_desc=True)
        status[dbsettings.Status.ONGOING.name] = \
            dbutils.get_sites_names_by_processing_status(s_status=dbsettings.Status.ONGOING, uuid=uuid, sorting_desc=True)
        status[dbsettings.Status.ERROR.name] = \
            dbutils.get_sites_names_by_processing_status(s_status=dbsettings.Status.ERROR, uuid=uuid, sorting_desc=True)
        status[dbsettings.Status.ERROR_DEFUNC.name] = \
            dbutils.get_sites_names_by_processing_status(s_status=dbsettings.Status.ERROR_DEFUNC, uuid=uuid, sorting_desc=True)
        status[dbsettings.Status.DISCARDED.name] = \
            dbutils.get_sites_names_by_processing_status(s_status=dbsettings.Status.DISCARDED, uuid=uuid, sorting_desc=True)
        status[dbsettings.Status.FINISHED.name] = \
            dbutils.get_sites_names_by_processing_status(s_status=dbsettings.Status.FINISHED, uuid=uuid, sorting_desc=True)
        status[dbsettings.Status.DISCOVERING.name] = \
            dbutils.get_sites_names_by_processing_status(s_status=dbsettings.Status.DISCOVERING, uuid=uuid, sorting_desc=True)

    return status


def generate_uuid():

    """
    Generate UUID from current timestamp and MAC address

    :return: UUID - UUID (https://docs.python.org/2/library/uuid.html)
    """

    return uuid.uuid1()


def get_type_site(site):
    """
    Returns the type of site based on the site received

    :param uuid: str - Site
    :return: dbsettings.Type
    """
    URL_REGEX = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|\
        pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|\
        cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|\
        hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|\
        mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|\
        sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|\
        zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|\
        net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|\
        az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|\
        er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|\
        kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|\
        no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|\
        td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""
    
    I2P_REGEX = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:i2p)/)\
        (?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:i2p)\b/?(?!@)))"""

    FREENET_REGEX = r"""((((127.0.0.1|localhost):8888/){0,1}(freenet:){0,1}(USK|SSK|CHK)@[a-zA-Z0-9~\-]{43},[a-zA-Z0-9~\-]{43},(AQACAAE|AQABAAE|AQECAAE|AAMC--8|AAIC--8|AAICAAA)/[a-zA-Z0-9\-\._%?\\& ]{0,150})/?[0-9\-]{0,10})/?(.*)"""

    ONION_REGEX = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:onion)/)\
        (?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:onion)\b/?(?!@)))"""

    if bool(re.search(FREENET_REGEX, site)):
        return dbsettings.Type.FREENET
    elif bool(re.search(I2P_REGEX, site)):
        return dbsettings.Type.I2P
    elif bool(re.search(ONION_REGEX, site)):
        return dbsettings.Type.TOR
    elif bool(re.search(URL_REGEX, site)):
        return dbsettings.Type.SURFACE
    else:
        return dbsettings.Type.UNKNOWN

def compare_freesite(site):
    """
    Returns true if the site exists or false if the site doesnt exists

    :param uuid: str - Site
    :return: Bool
    """
    #Limpiar la barra final
    if site[-1] is "/":
        site = site[:-1]

    #Limpiar el caracter hashtag
    site = site.rsplit("#", 1)[0]

    #Comprobamos si es USK o SSK
    is_usk = False
    if "USK@" in site:
        is_usk = True
    
    #Seleccionamos lo de despues del arroba
    site_parse = site.split("@", 1)[1]

    if is_usk:
        site_parse = site_parse.rsplit("/", 1)[0]
    else:
        site_parse = site_parse.rsplit("-", 1)[0]

    number_freesites = dbutils.count_freesites(site_parse)
    if number_freesites >= 1:
        return True
    else:
        return False
    


