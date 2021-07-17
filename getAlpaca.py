from getTicker import GetTicker
from alpaca_trade_api.rest import REST
from alpaca_trade_api.rest import TimeFrame
import json
import sys
import logging


class GetAlpacaTicker(GetTicker):
    def __init__(self, tickerName, saveToFile):
        super(GetAlpacaTicker, self).__init__(tickerName, saveToFile)
        self.api = REST()
        logging.debug("Alpaca started. ")

    def run(self, start, end):
        try:
            quotes = self.api.get_bars(
                self.tickerName, TimeFrame.Hour, start, end, adjustment='raw').df
            if (self.saveToFile):
                with open("Alpaca-" + start + end + ".quotes", "w") as text_file:
                    text_file.write("%s" % quotes)
        except:
            logging.error("Unexpected error:", sys.exc_info()[0])
            raise SystemError(sys.exc_info()[0])
        return quotes, {'ticker': self.tickerName}
