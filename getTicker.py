import numpy as np

import logging

class GetTicker:
    def __init__(self, tickerName, saveToFile):
        self.tickerName = tickerName
        self.saveToFile = saveToFile

    def run(self):
        logging.debug("Please override - Starting GetTicker")

    def run(self, start, end):
        logging.debug(
            "def run(self, start, end):Starting GetTicker with start/end time and granularity")

    def getHistoricalTickDta(self, start, end, maxTradeCount, outfile):
        """
        function to get the historical tick data and save it in the file specified.

        Parameters
        ----------
        start: string
            start time, in string format (using srftime dd/mm/yyyy)
        end: string
            end time, in string format (using srftime dd/mm/yyyy)
        maxTradeCount: int
            total number of trades to be saved in this query.
        outFile: string
            filename where the data is stored. Could also be a handle to the database

        Return
        ------
        count of trades read.

        """
        logging.debug("override this function to be able to get the historical data saved in a file.")

    def processHistoricalData(self, fileName):
        """
        parse the historical data provided into a custom format and and save into a database for further usage.
        """
        logging.debug(
            "override this function to be able to process the historical data saved in a file.")
