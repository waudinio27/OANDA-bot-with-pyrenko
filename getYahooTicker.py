from getTicker import GetTicker
import yfinance as yf
import json
import sys
import logging


class GetYahooTicker(GetTicker):
    def __init__(self, tickerName, startTime, endTime):
        super(GetYahooTicker, self).__init__(tickerName, startTime, endTime)
        logging.debug("start yahoo fetch: " + tickerName)

    def run(self):
        instrument = yf.Ticker(self.tickerName)

        try:
            # get stock info
            information = instrument.info
            logging.debug("Instrument info -"+self.tickerName +
                          ": " + json.dumps(information))
            # get historical market data
            hist = instrument.history(period="1d", interval='1m')
            logging.debug(hist)
            # show actions (dividends, splits)
            instrument.actions
        except:
            logging.error("Unexpected error:", sys.exc_info()[0])
