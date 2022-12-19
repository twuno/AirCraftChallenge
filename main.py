# coding=utf-8
# This is a sample Python script.
from collections import OrderedDict

from htmlParser import Parser
from xlsManager import xlsManager
from configManager import configManager
from webPetition import Petition
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def TailInfo(name):

    dict = OrderedDict({})##{ 'Tail Number':'Not Found', 'Serial Number':'Not Found', 'Manufacturer':'Not Found', 'Model':'Not Found', 'Engine Model':'Not Found', 'Registered Owner Name':'Not Found'}
    # Use a breakpoint in the code line below to debug your script.
    cf = configManager()
    file = cf.getKey("file")
    excl = xlsManager(file)
    lista = excl.getTailList()

    wP=Petition()
    fields= cf.getKey('keys')
    for field in fields:
        dict[field]='Not Found'
    #print cf.getKey('src')
    for item in lista:

        html = wP.getPetition2(item[0])
        help = Parser(dict,item[0])
        info = help.dicGenerator(html).copy()
        excl.saveRow(info)
    excl.saveFile()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    TailInfo('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
