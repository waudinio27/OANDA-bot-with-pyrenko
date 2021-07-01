import numpy as np

import logging

class GetTicker:
    def __init__(self, tickerName, startTime, endTime):
        self.tickerName = tickerName
        self.startTime = startTime
        self.endTime = endTime

    def run(self):
        logging.debug("Starting GetTicker")
