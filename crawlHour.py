
# python initLog.py postgres r2tadmiadc localhost 5432
# python crawlHour.py postgres r2tadmiadc localhost 5432

# import essential modules
import os 
import sys
import json
import requests
import pandas as pd
from os import listdir, stat
from typing import List, Dict
from colorama import init, Fore, Back, Style
init(convert=True)

# import main functionality
from src.dbcontext import Dbcontext
from src.requester import Requester
from src.utils import UrlBundler, Key

red = "notDownloaded"
green = "downloaded"

start = "2021-01-01 00:00:00" 
end = "2021-01-31 23:59:59"



if __name__ == "__main__":
    # initialize basic object.
    myKey = Key()
    myBundler = UrlBundler()
    myReq = Requester(myBundler, myKey)

    # initialize dbcontext
    myDBcontext = Dbcontext({"user":str(sys.argv[1]), 
                            "password":str(sys.argv[2]), 
                            "host":str(sys.argv[3]), 
                            "port":str(sys.argv[4])}, "sensordata")

    # load enum
    data = pd.read_csv(r"logging/january_log.csv")
    

    for i in range(0, 2): #data.shape[0]
        [projectID, projectKey, deviceId, item, status] = list(data.iloc[i])
        statusString = str(projectID) + " " + str(deviceId) + " " + str(item)
        statusString = statusString.ljust(30)
        if status == red:
            try:
                returnData = myReq.getHourData({
                    "projectKey": projectKey,
                    "deviceId": deviceId,
                    "item": item,
                    "start": start,
                    "end": end
                })
            

                data.iloc[i, data.columns.get_loc('status')] = "downloaded"
                data.to_csv(r"logging/january_log.csv", index=False)
                print(Style.RESET_ALL + Fore.LIGHTGREEN_EX + statusString + " success!" )
            except Exception as e:
                print(Style.RESET_ALL + Fore.RED + statusString + " failed!" )
                print(e)
        else:
            print(Style.RESET_ALL + Fore.YELLOW + statusString + " already done!" )
        
        
    
    

