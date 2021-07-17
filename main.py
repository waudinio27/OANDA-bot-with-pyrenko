import datetime
from getAlpaca import GetAlpacaTicker
from dbAccess  import DbAccess
import logging

def main():
    #TODO: move logging config to config file
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename='log/program.log',
                        level=logging.DEBUG)
    logging.info('Program Started')
    currentDate = datetime.datetime.today()
    prevDate = datetime.datetime.today() - datetime.timedelta(days=1)

    tickerApp = GetAlpacaTicker("MSFT", True)
    bars = tickerApp.run(prevDate.strftime("%Y-%m-%d"),
                         currentDate.strftime("%Y-%m-%d"))

    logging.info('Program Finished\r\n' + bars)

if __name__ == '__main__':
    main()
