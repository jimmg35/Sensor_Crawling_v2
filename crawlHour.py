
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
from src.Parser import HourParser 
from src.dbcontext import Dbcontext
from src.requester import Requester
from src.utils import UrlBundler, Key



red = "notDownloaded"
green = "downloaded"

start = "2021-01-01 00:00:00" 
end = "2021-01-31 23:59:59"

no_voc_projects = ["709", "1071", "1072"]

start_month = "01"

if __name__ == "__main__":
    # initialize basic object.
    myKey: Key = Key()
    myBundler = UrlBundler()
    myReq = Requester(myBundler, myKey)

    # initialize dbcontext
    myDBcontext = Dbcontext({"user":str(sys.argv[1]), 
                            "password":str(sys.argv[2]), 
                            "host":str(sys.argv[3]), 
                            "port":str(sys.argv[4])}, "sensordata")

    # load enum
    data = pd.read_csv(r"logging/january_log.csv")
    

    for i in range(0, 5): #data.shape[0]
        [projectID, projectKey, deviceId, status] = list(data.iloc[i])
        statusString = str(projectID) + " " + str(deviceId)
        statusString = statusString.ljust(30)
        
        if str(projectID) in no_voc_projects:
            hasVoc = False
            sensor_items = ["pm2_5", "humidity", "temperature"]
        else:
            hasVoc = True
            sensor_items = ["voc", "pm2_5", "humidity", "temperature"]
        

        if status == red:
            try:
                # request
                data_list = [myReq.getHourData({
                    "projectKey": projectKey,
                    "deviceId": deviceId,
                    "item": j,
                    "start": start,
                    "end": end}) for j in sensor_items]
                # parse
                total_chunk_np = HourParser.parseHourData(data_list, deviceId, hasVoc)
                # import into database
                myDBcontext.ImportHourData(total_chunk_np, {
                    "porjectId": str(projectID),
                    "startMonth": start_month
                })



                data.iloc[i, data.columns.get_loc('status')] = "downloaded"
                data.to_csv(r"logging/january_log.csv", index=False)
                print(Style.RESET_ALL + Fore.LIGHTGREEN_EX + statusString + " success!" )
            except Exception as e:
                print(Style.RESET_ALL + Fore.RED + statusString + " failed!" )
                print(e)
        else:
            print(Style.RESET_ALL + Fore.YELLOW + statusString + " already done!" )
        
        
    
    

