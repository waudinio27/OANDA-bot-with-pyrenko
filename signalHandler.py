import signal
import time
import logging

#TODO: catch exit and write db to disk
class handleKill:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, *args):
    self.kill_now = True

if __name__ == '__main__':
  killer = handleKill()
  while not killer.kill_now:
    time.sleep(1)
    logging.debug("doing something in a loop ...")
   
  logging.debug("End of the program. I was killed gracefully :)")