from getYahooTicker import GetYahooTicker
from dbAccess  import DbAccess
from duckdb import DuckDb

import logging

def main():
    #TODO: move logging config to config file
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename='log/program.log',
                        level=logging.DEBUG)
    logging.info('Program Started')
    tickerApp = GetYahooTicker("MSFT", "", "")
    tickerApp.run()

    logging.info('Program Finished')

if __name__ == '__main__':
    main()
