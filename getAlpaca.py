from getTicker import GetTicker
from alpaca_trade_api.rest import REST
from alpaca_trade_api.rest import TimeFrame
import json
import sys
import logging
import pandas as pd

class GetAlpacaTicker(GetTicker):
    """
    Setup a ticker for read using Alpaca api.
    Each ticker returned by the Alpaca Api has the following fields:
    Historical Data
    ---------------
        Properties (https://alpaca.markets/docs/api-documentation/api-v2/market-data/alpaca-data-api-v2/historical/)
        #t : stringRequired :        Timestamp in RFC-3339 format with nanosecond precision.
        #x : stringRequired :        Exchange where the trade happened.
        #p : numberRequired :        Trade price.
        #s : intRequired    :        Trade size.
        #c : array<string>Required : Trade conditions.
        #i : intRequired           : Trade ID.
        #z : stringRequired        : Tape.
    """
    def __init__(self, tickerName, saveToFile):
        super(GetAlpacaTicker, self).__init__(tickerName, saveToFile)
        self.api = REST()
        logging.debug("Alpaca started. ")

    def run(self, start, end):
        try:
            quotes = self.api.get_bars(
                self.tickerName, TimeFrame.Hour, start, end, adjustment='raw').df
            if (self.saveToFile):
                with open("Alpaca-" + self.tickerName + "-" + start + "_"+ end + ".quotes", "w") as text_file:
                    text_file.write("%s" % quotes)
        except:
            logging.error("Unexpected error:", sys.exc_info()[0])
            raise SystemError(sys.exc_info()[0])
        return quotes, {'ticker': self.tickerName}

    def getHistoricalTickDta(self, start, end, maxTradeCount, outfile):
        logging.info(f"get historical data for the period - {start}, {end}; max ticks - {maxTradeCount}")
        if (self.testMode == False):
            try:
                trades = self.api.get_trades(self.tickerName, start, end, maxTradeCount)
            except:
                logging.error("could not get tickers", sys.exc_info()[0])
        else:
            try:
                with open(self.testModeInputFile, "r") as text_file:
                    trades = text_file.read()
                with open(outfile, "w") as text_file:
                    text_file.write("%s" % trades)
            except:
                logging.error("could not save to file.", sys.exc_info()[0])
        return trades.count('Trade')

    def setTestMode(self, mode, **kwargs):
        """
        Set the test mode of the class (in test mode no queries are made to the external world, only the local files supplied as test files are read.)
        Add additional arguments, if required.
        In case of changing mode to testMode, an input file is required to be able to read and pass the data to the caller in the output file.
        TODO: change this call to use file handles instead of names, so that database handles could also be passed.
        """
        self.testMode = mode
        fileName = kwargs.get('fileName')
        if (fileName):
            self.testModeInputFile = fileName

    def processHistoricalData(self, fileName):
        """
        parse the historical data provided into a custom format and and save into a database for further usage.
        This is required because the data currently is sourced from different data sources, because I dont have a fixed 
        source of truth.
        """
        logging.info(f"process historical data from file - {fileName}")
        with open(fileName, "r") as text_file:
            trades = text_file.read()

        ##df = pd.json_normalize(trades['Trade'])
        return trades
"""
async def trade_callback(t):
    print('trade', t)


async def quote_callback(q):
    print('quote', q)


# Initiate Class Instance
stream = Stream(<ALPACA_API_KEY>,
                <ALPACA_SECRET_KEY>,
                base_url=URL('https://paper-api.alpaca.markets'),
                data_feed='iex')  # <- replace to SIP if you have PRO subscription

# subscribing to event
stream.subscribe_trades(trade_callback, 'AAPL')
stream.subscribe_quotes(quote_callback, 'IBM')

stream.run()

"""
