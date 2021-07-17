from pystoredb import PyStoreDb
import logging

class DBFactory:
    @staticmethod
    def newInstance(name):
        return {
            "pystore": PyStoreDb()
        }[name]
