import logging


class DbAccess:
    dbFile = None
    name = None
    connection = None
    thisInstance = None
 
    def __init__(self, dbFile, instanceName):
        if DbAccess.thisInstance is not None:
            if DbAccess.dbFile != dbFile:
                raise Exception("I dont support two databases at present")
            else:
                thisInstance = self
        if DbAccess.name is not None:
            name = instanceName

    def stop(cls):
        logging.debug("Stopping database")

    def start(cls):
        logging.debug("Starting database")

    def store(self, store, ticker, data, dataInfo):
        logging.debug("dbAccess store")
