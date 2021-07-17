import pandas as pd
from getAlphaVantage import GetAlphaVantageTicker
import pathlib
import sys

parentDir = pathlib.Path(__file__).parent.resolve().parent.parent.absolute()
sys.path.append(parentDir)
sys.path.append("..")

from getYahooTicker import GetYahooTicker
from dbAccess import DbAccess
from pystoredb import PyStoreDb

import logging


def main():
    #TODO: move logging config to config file
    print (parentDir)
    logging.basicConfig(format='%(asctime)s %(lPevelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename=__file__ + '.log',
                        level=logging.DEBUG)
    logging.info('Program Started')
    tickerApp = GetAlphaVantageTicker("MSFT", True)
    data, metaData = tickerApp.run()

    # ## save in a file using pystore
    dbOOject = PyStoreDb("./tickers.db", "testTickers")
    storeName = "AlphaVantage"
    dbOOject.start(storeName)
    dbOOject.store(storeName, "MSFT", data, "testTickers")
    readData = dbOOject.read(storeName, "MSFT", "", "")
    pd.set_option("display.max_rows", None, "display.max_columns", None)

    logging.info("read data from store: \r\n" + readData)
    if(data != readData):
        logging.error("data could not be read correctly")
    dbOOject.stop

if __name__ == '__main__':
    main()
