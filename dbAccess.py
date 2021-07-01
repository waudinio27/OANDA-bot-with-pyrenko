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

    @classmethod
    def stop(cls):
        logging.debug("Stopping database")

    @classmethod
    def start(cls):
        logging.debug("Starting database")

    @classmethod
    def instance(cls, dbFile, instanceName ):
        logging.debug("Get/create database instance")
        if cls.thisInstance is None:
            instance = cls(dbFile, instanceName)
        return instance

    @classmethod
    def getInstance(cls):
        logging.debug("Get database instance")
        return cls.thisInstance
