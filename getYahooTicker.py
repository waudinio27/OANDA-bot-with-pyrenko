from getTicker import GetTicker
import yfinance as yf
import json

import logging

class GetYahooTicker(GetTicker):
    def __init__(self, tickerName, startTime, endTime):
        super(GetYahooTicker, self).__init__(tickerName, startTime, endTime)
        logging.debug("start yahoo fetch: " + tickerName)

    def run(self):
        instrument = yf.Ticker(self.tickerName)

        # get stock info
        information = instrument.info
        logging.debug("Instrument info -"+self.tickerName +
                      ": " + json.dumps(information))
        # get historical market data
        """
        :Parameters:
            period : str
                Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                Either Use period parameter or use start and end
            interval : str
                Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                Intraday data cannot extend last 60 days
            start: str
                Download start date string (YYYY-MM-DD) or _datetime.
                Default is 1900-01-01
            end: str
                Download end date string (YYYY-MM-DD) or _datetime.
                Default is now
            prepost : bool
                Include Pre and Post market data in results?
                Default is False
            auto_adjust: bool
                Adjust all OHLC automatically? Default is True
            back_adjust: bool
                Back-adjusted data to mimic true historical prices
            proxy: str
                Optional. Proxy server URL scheme. Default is None
            rounding: bool
                Round values to 2 decimal places?
                Optional. Default is False = precision suggested by Yahoo!
            tz: str
                Optional timezone locale for dates.
                (default data is returned as non-localized dates)
            **kwargs: dict
                debug: bool
                    Optional. If passed as False, will suppress
                    error message printing to console.
        """

        hist = instrument.history(period="1d", interval='1m')
        logging.debug(hist)
        # show actions (dividends, splits)
        instrument.actions
