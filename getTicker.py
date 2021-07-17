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
