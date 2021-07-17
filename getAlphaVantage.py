from getTicker import GetTicker
from alpha_vantage.timeseries import TimeSeries
import json
import sys
import logging


class GetAlphaVantageTicker(GetTicker):
    def __init__(self, tickerName, saveToFile):
        super(GetAlphaVantageTicker, self).__init__(tickerName, saveToFile)
        with open('/root/alphaVantage.key', 'r') as f:
                        self.apiKey = f.read()
        logging.debug("read AVantage - api key: ")

    def run(self):
        ts = TimeSeries(key=self.apiKey, output_format='pandas')

        try:
            data, metaData = ts.get_intraday(
                self.tickerName, interval='1min', outputsize='full')
        except:
            logging.error("Unexpected error:", sys.exc_info()[0])
        return data, metaData
