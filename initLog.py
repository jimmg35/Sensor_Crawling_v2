# import essential modules
import requests
import os 
import sys
import json
from typing import List, Dict
import pandas as pd

# import main functionality
from src.dbcontext import Dbcontext
from src.utils import UrlBundler, Key
from src.requester import Requester




if __name__ == "__main__":
    if os.path.exists(r"logging/january_log.csv"):
        os.remove(r"logging/january_log.csv")

    # initialize basic object.
    myKey = Key()
    myBundler = UrlBundler()
    myReq = Requester(myBundler, myKey)

    # initialize dbcontext
    myDBcontext = Dbcontext({"user":str(sys.argv[1]), 
                            "password":str(sys.argv[2]), 
                            "host":str(sys.argv[3]), 
                            "port":str(sys.argv[4])}, "sensordata")
    
    # query metadata from database
    rawdata = myDBcontext.queryDeviceSensorMeta_fixed()

    #sensor_items = ["voc", "pm2_5", "humidity", "temperature"]

    with open(r"logging/january_log.txt", 'w') as f:
        f.writelines("projectId,projectKey,deviceId,status\n")

        for index_i, i in enumerate(rawdata):
            if index_i == len(rawdata)-1:
                f.writelines(str(i[0])+','+i[1]+','+str(i[2])+',notDownloaded')
            else:
                f.writelines(str(i[0])+','+i[1]+','+str(i[2])+',notDownloaded\n')


    os.rename(r"logging/january_log.txt", r"logging/january_log.csv")