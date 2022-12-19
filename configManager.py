import json
#class to manage the json config
class configManager():

    def __init__(self):
        with open("info.json",'r') as jsonfile:
            self.__data =json.load(jsonfile)

    def getKey(self,key):
        return self.__data[key]

