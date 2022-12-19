import urllib2
import ssl
from StringIO import StringIO
import gzip

#class to get the html file

import requests as requests

from configManager import configManager

class Petition():
    __dir=''

    def __init__(self):
        self.__cf = configManager()



    def getPetition2(self,name):
        src = self.__cf.getKey("src")
        path = src + '/' + name
        r =requests.get(path)
        return r.text