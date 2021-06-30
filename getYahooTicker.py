from getTicker import GetTicker
import yfinance as yf

import logging
logger = logging.getLogger(__name__)

class GetYahooTicker(GetTicker):
    def __init__(self, tickerName, startTime, endTime):
        super().__init__(tickerName, startTime, endTime)
        # self.tickerName = tickerName
        # self.startTime = startTime
        # self.endTime = endTime
        logger.debug("start" + tickerName )

    def run(self):
        msft = yf.Ticker("GOOGL")

        # get stock info
        msft.info

        # get historical market data
        hist = msft.history(period="max")
        logger.debug(hist)
        # show actions (dividends, splits)
        msft.actions
