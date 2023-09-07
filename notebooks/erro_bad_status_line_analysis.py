#!/usr/bin/env python
# coding: utf-8

# ### Análisis del error en conexiones HTTP: BadStatusLine

# In[62]:


import pandas as pd
import subprocess
import requests
import shlex
import traceback
import matplotlib.pyplot as plt

# For saving dataframes
data_path = 'data/error_bad_status_line/'


# In[42]:


def connectThroughProxy(eepsite_url, proxies, timeout):
    '''
    Connection through HTTP i2p proxy
    '''
    # headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}
    response = requests.get(eepsite_url, proxies=proxies, headers=headers, timeout=timeout)
    return response


# In[43]:


def printResponse(response):
    '''
    HTTP response printing
    '''
    print((response.status_code))
    print((response.elapsed.total_seconds()))
    print((response.headers))


# In[44]:


### Get all i2p peers who raise the error
host='i2pProjectM2'
with open(data_path + host + '_bad_status_line.txt','r') as f:
    bsl = f.readlines()
    
# Filtering lines
bsl=[item.replace(':','').replace('\n','') for item in bsl]


# In[45]:


proxies={'http': 'http://localhost:4444'}
timeout=30

site_error = {}

for site in bsl:
    try:
        url='http://'+site
        print(("[+] Connecting to " + url))

        response = connectThroughProxy(url, proxies, timeout)
        printResponse(response)
        

    except Exception as e:
        print(e)  
        site_error[site]=e
        
    print("")
        


# In[66]:


for site in list(site_error.keys()):
    command="ncat -v --proxy localhost:4444 "+ site
    print(("[+] " + str(command)))
    p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    print(output)
    print("")


# In[ ]:




