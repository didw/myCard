#!/usr/bin/python
# -*- coding: utf-8 -*-
from myCard import *
import json
import pickle
import os



def main(fname):
  app = Application()
  app.connect(title="Yang-s6")
  dlg = app.Yangs6
  from pywinauto.timings import TimeConfig
  #time_config = TimeConfig()
  #time_config.Fast()
  for i in range(1000):
    print(i)
    dlg.ClickInput(coords=(450, 885))
    dlg.ClickInput(coords=(450, 785))
    dlg.ClickInput(coords=(66, 785))
    if i%100 == 0:
      time.sleep(5)


if __name__ == '__main__':
  fname = '../kra/result/1708/26.pkl'
  main(fname)
  




#app.Yangs6.ClickInput(coords=(260, 490))


