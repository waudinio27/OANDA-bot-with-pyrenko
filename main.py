from getYahooTicker import GetYahooTicker
import logging

def main():
    #TODO: move logging config to config file
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='log/program.log', level=logging.INFO)
    logging.info('Program Started')
    tickerApp = GetYahooTicker("MSFT", "", "")
    tickerApp.run()

    logging.info('Program Finished')

if __name__ == '__main__':
    main()
