#!/usr/bin/python
# -*- coding: utf-8 -*-
from myCard import *
import json
import pickle


def verify_bet_list(bet_list):
  for day in ['Sat', 'Sun']:
    bet_list_day = bet_list[day]
    for rcno in range(1, 16):
      if rcno not in bet_list_day:
        continue
      bet_rc = bet_list_day[rcno]
      for target in bet_rc:
        print("Day: %s, rcno: %d, target: %d, %d, %d,  value: %d" %
              (day, rcno, *list(target), bet_rc[target]))


def main():
  app = Application()
  app.connect(title="Yang-s6")
  dlg = app.Yangs6
  my_card = MyCard(dlg)

def remap_keys(mapping):
  return [{'key':k, 'value': v} for k, v in mapping.items()]

def test_load_bet_list():
  bet_list = {'Sat': { 1: {(1,2,3): 1, 
                           (1,2,4): 1, 
                           (1,3,4): 1, 
                           (5,2,4): 1},
                       2: {(1,2,3): 1, 
                           (1,2,4): 1, 
                           (1,3,4): 1, 
                           (5,2,4): 1},
                       3: {(1,2,3): 1, 
                           (1,2,4): 1, 
                           (1,3,4): 1, 
                           (5,2,4): 1},
                      10: {(1,2,3): 1, 
                           (1,2,4): 1, 
                           (1,3,4): 1, 
                           (5,2,4): 1},
                      },
              'Sun': { 1: {(1,2,3): 1, 
                           (1,2,4): 1, 
                           (1,3,4): 1, 
                           (5,2,4): 1},
                       2: {(1,2,3): 1, 
                           (1,2,4): 1, 
                           (1,3,4): 1, 
                           (5,2,4): 1},
                       3: {(1,2,3): 1, 
                           (1,2,4): 1, 
                           (1,3,4): 1, 
                           (5,2,4): 1},
                      10: {(1,2,3): 1, 
                           (1,2,4): 1, 
                           (1,3,4): 1, 
                           (5,2,4): 1},
                      }
              }
  return bet_list

if __name__ == '__main__':
  #main()
  bet_list = test_load_bet_list()
  verify_bet_list(bet_list)
  pickle.dump(bet_list, open('bet_list.pkl', 'wb'))
  bet_list2 = pickle.load(open('bet_list.pkl', 'rb'))
  verify_bet_list(bet_list2)




#app.Yangs6.ClickInput(coords=(260, 490))


