import pyexcel as p
from configManager import configManager

#Class to get the itemList, manage records and Write on xls file,
class xlsManager():
    def __init__(self,dir):
        self.__fileName =dir
        self.__finalDoc=[]

    def getTailList(self):
       records= p.get_sheet(file_name=self.__fileName, start_column=0, column_limit=1,start_row=1)
       return records

#Save Record on the Actual List
    def saveRow(self, dic):
        dic.pop(u'Name','Name')
        self.__finalDoc.append(dic)

#Stored all the records on File
    def saveFile(self):
        cf = configManager()
        file = cf.getKey('file')
        p.save_as(records=self.__finalDoc, dest_file_name=file)
