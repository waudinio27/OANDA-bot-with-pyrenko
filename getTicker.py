import numpy as np

import logging

class GetTicker:
    def __init__(self, tickerName):
        self.tickerName = tickerName

    def run(self):
        logging.debug("Starting GetTicker")
