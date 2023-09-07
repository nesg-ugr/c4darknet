import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sb
from sqlalchemy import create_engine


# Experiment id for saving it
experiment_id = 'experiment_07062019_1900'
# For saving dataframes
data_path = 'data/experiment/' + experiment_id + '/bbdd/'
# Saving the experiment: 1 --> to keep the results on file system
to_save = 1
# Getting the experiment: 1 --> restore, 0 --> gets from database
from_fs = 0
# local or remote data base access: 1 --> local, 0 --> remote
bbdd_connection = 1

if bbdd_connection:
  port = '3306'
else:
  port = '6666'
engine = create_engine('mysql+pymysql://i2p:4=XoG!*L@localhost:'+port+'/i2p_database', echo=False)
print("[+] Dumping site table ...")
df_site = pd.read_sql_query('select * from site', engine, chunksize=10000)
print("[+] Dumping sitestatus table ...")
df_status = pd.read_sql_query('select * from sitestatus', engine)
print("[+] Dumping sitesource table ...")
df_source = pd.read_sql_query('select * from sitesource', engine)
print("[+] Dumping siteprocessinglog table ...")
#df_logprocessing = pd.read_sql_query('select * from siteprocessinglog', engine, chunksize=1000000)
print("[+] Dumping sitelanguage table ...")
df_language = pd.read_sql_query('select * from sitelanguage', engine)
print("[+] Dumping sitehomeinfo table ...")
df_sitehomeinfo = pd.read_sql_query('select * from sitehomeinfo', engine)
print("[+] Dumping siteconnectivitysummary table ...")
df_connectivity = pd.read_sql_query('select * from siteconnectivitysummary', engine)
    
## Saving the results of experiments

if to_save:
    print(("[+] Saving results to {0}".format(data_path + experiment_id)))
    df_site.to_pickle(data_path + experiment_id + "_site.pickle")
    df_status.to_pickle(data_path + experiment_id + "_status.pickle")
    df_source.to_pickle(data_path + experiment_id + "_source.pickle")
    #df_logprocessing.to_pickle(data_path + experiment_id + "_logprocessing.pickle")
    df_language.to_pickle(data_path + experiment_id + "_sitelanguage.pickle")
    df_sitehomeinfo.to_pickle(data_path + experiment_id + "_sitehomeinfo.pickle")
    df_connectivity.to_pickle(data_path + experiment_id + "_siteconnectivity.pickle")


