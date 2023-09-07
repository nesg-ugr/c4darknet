# -*- coding: utf-8 -*-

"""
    :mod:`request_conn`
    ===========================================================================
    :synopsis: HTTP requests and responses
    :author: Roberto Magán Carrión
    :contact: roberto.magan@uca.es, rmagan@ugr.es, robertomagan@gmail.com
    :organization: University of Cádiz, University of Granada
    :project: I2P Crawler
    :since: 0.0.1
"""

import requests

def connectThroughProxy(darksite_url, proxies, timeout):
    # headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}
    darksite_url = darksite_url.replace("@", "%40")
    response = requests.get(darksite_url, proxies=proxies, headers=headers, timeout=timeout)
    return response
    '''
    try:
        response = requests.get(darksite_url, proxies=proxies, headers=headers, timeout=timeout)
    except requests.exceptions.HTTPError as errh:
        return errh
        #print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        return errc
        #print ("Error Connecting:",errc)
    except requests.exceptions.ReadTimeout as errrt:
        return errrt
    except requests.exceptions.Timeout as errt:
        return errt
        #print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        return err
        #print ("OOps: Something Else",err)
    
    return response
    '''
