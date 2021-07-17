from typing import Collection
from dbAccess import DbAccess
import pystore

import logging


"""
# Following datastores are assumed:
# 1. Raw datastore --> fetch from source and save
# 2. Datastore for each type of strategy input (e.g. AO, renko bricks etc..)
# heirarchy:
    store --> complete data set for a ticker
        |_ collection Daily data fetch?
        |_ momentum data has to be derived based on the time interval selected
            -- therefore no data save is required for the same.
            -- anyways the datastore should also be agnostic to what data
               is being fed to it. It should only store timeseries data.

"""


class PyStoreDb(DbAccess): 
    def __init__(self, dbFile, instanceName):
        super(PyStoreDb, self).__init__(dbFile, instanceName)
        pystore.set_path(dbFile)
        self.storeList = {}

    def stop(self):
        logging.debug("nothing to stop - file database")

    def start(self, storeName):
        logging.debug("initialize pystore - file database")
        self.storeList[storeName] = pystore.store(storeName)

    def store(self, storeName, ticker, data, dataInfo):
        collection = self.storeList[storeName].collection(ticker)
        collection.write(ticker, data, metadata={'source': dataInfo})

    def read(self, storeName, ticker, startTime, endTime):
        self.storeList[storeName] = pystore.store(storeName)
        collection = self.storeList[storeName].collection(ticker)
        return collection.item(ticker).data
