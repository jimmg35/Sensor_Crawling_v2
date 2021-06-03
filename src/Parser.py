import os 
from os import listdir
import numpy as np 
import pandas as pd

# deviceid, voc, pm2_5, humidity, temperature, date, hour, minute


class Parser():
    def __init__(self):
        self.column_array = ["DEVICE_ID", "VOC()", "PM2_5(µg/m3)", "HUMIDITY_MAIN(%)", "TEMPERATURE_MAIN(℃)", "TIME"]

    def parseProjectMonthData(self, data_path, output_path):
        """
            put all csv files(a project, a month) into folder(data_path)
        """
        total_data_chunk = []
        for index, csvFile in enumerate(listdir(data_path)):
            file_path_string = self.formatFileString(csvFile, index)
            file_path = os.path.join(data_path, file_path_string)
            data = pd.read_csv(file_path)
            data_chunk = []
            for column in self.column_array:
                data_chunk.append(list(data[column]))
            data_chunk = np.array(data_chunk)
            total_data_chunk.append(data_chunk.T)
        total_data = self.mergeAllTable(total_data_chunk)
        print(total_data)
        print(total_data.shape)
    
    def mergeAllTable(self, total_data_chunk):
        return np.vstack(total_data_chunk)
    
    def formatFileString(self, csvFile, index):
        file_path_string = ""
        for i in csvFile.split('_')[0: len(csvFile.split('_'))-1]:
            file_path_string += i + '_'
        file_path_string += "{}.csv".format(index)
        return file_path_string