import datetime
from getAlpaca import GetAlpacaTicker
from dbAccess  import DbAccess
import logging
import pandas as pd


def main():
    #TODO: move logging config to config file
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename='log/program.log',
                        level=logging.DEBUG)
    logging.info('Program Started')
    currentDate = datetime.datetime.today() - datetime.timedelta(days=30)
    prevDate = datetime.datetime.today() - datetime.timedelta(days=60)

    # save historical data for backtesting

    tickerApp = GetAlpacaTicker("MSFT", False)
    tickerApp.setTestMode(True, fileName="Alpaca-ticker.quotes")
    totalTicksRead = tickerApp.getHistoricalTickDta(prevDate.strftime("%Y-%m-%d"),
                         currentDate.strftime("%Y-%m-%d"), 10000, "Alpaca-ticker-new.quotes")

    pandasFrames = tickerApp.processHistoricalData("Alpaca-ticker-new.quotes")
    pd.set_option("display.max_rows", None,
                            "display.max_columns", None)
    logging.info(pandasFrames)

    logging.info('Program Finished\r\n' + str(totalTicksRead))

if __name__ == '__main__':
    main()
