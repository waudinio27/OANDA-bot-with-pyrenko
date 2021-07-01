from dbAccess import DbAccess
import duckdb
import logging

class DuckDb(DbAccess):
    def __init__(self, dbFile, instanceName):
        super(DuckDb, self).__init__(dbFile, instanceName)

    @classmethod
    def stop():
        logging.debug("Stopping database")

    @classmethod
    def start():
        logging.debug("Starting database")
        DbAccess.connection = duckdb.connect(
            database=':memory:', read_only=False)
