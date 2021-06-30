import numpy as np

import logging
logger = logging.getLogger(__name__)

class GetTicker:
    def __init__(self, tickerName, startTime, endTime):
        self.name= tickerName
        self.startTime = startTime
        self.endTime = endTime

    def run(self):
        logger.debug("Starting GetTicker")
