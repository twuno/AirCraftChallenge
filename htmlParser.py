from HTMLParser import HTMLParser

class Parser(HTMLParser):
    __thisInfo = {}
    __flag = 0  # type: int
    __storeFlag = 0
    __TempKey = ''

    def __init__(self,dict,tailNumber):
            self.reset()
            self.__tailNumber= tailNumber
            self.__lista = dict
            #self.__dicGenerator(html)

    def dicGenerator(self,html):
        self.feed(html)
        self.__lista['Tail Number']=self.__tailNumber
        return self.__lista


    def handle_starttag(self, tag, attrs):

        if tag=='td': #Each open td tag turn on a flag, to verify the data
            self._setFlag(1)

    def handle_data(self, data):
        if self._getFlag()==1: #each data we found we verify if this is part of a td tag

            if data in self.__lista:  #If the data is part of the interest list, we start a flag to stored the next data
                self.__storeFlag=1
                self.__TempKey = data if not data=="Name" else "Registered Owner Namer"
            elif self.__storeFlag==1: #if the data isn't in the list but the storeFlag is on, is the value of the last key
                self.__lista[self.__TempKey]=data.strip() if not data.strip()=='' else "Not Found"
                self.restoreFlag( )
            self._setFlag(  0)

    def restoreFlag(self):
        self.__TempKey=''
        self.__storeFlag=0

    def handle_endtag(self, tag):
       #print 'fin tag',tag
       if tag == 'td':
            self._setFlag(0)
       if tag == 'tr' and self.__storeFlag==1: #if got a close tr tag and the storeFlag is on, our value were empty
           self.restoreFlag()


    def _setFlag(self,value):
        self.__flag = value

    def _getFlag( self):
        return self.__flag



