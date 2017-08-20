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

def load_dict(fname):
  return pickle.load(open(fname, 'rb'))


def betting(my_card, res_dict):
  # Bet sat first
  first = True
  for Day in ['Sat', 'Sun']:
    for rcno in range(1, 16):
      rc_dict = res_dict[Day][rcno]
      length_dict = len(rc_dict)
      if length_dict == 0:
        continue
      my_card.click_day(Day)
      my_card.click_rcno(rcno)
      my_card.click_next()
      if not first:
        my_card.click_confirm()
      time.sleep(2)
      head = 1
      for cand, value in rc_dict.items():
        #value = rc_dict[cand]
        my_card.click_head(head)
        my_card.click_ss()
        for j in range(3):
          my_card.click_hrno(j, cand[j])
        my_card.click_bet_total(value/100)
        length_dict -= 1
        head += 1
        if length_dict == 0 or head > 3:
          head = 1
          my_card.click_buy()
          time.sleep(3)
          if length_dict != 0:
            my_card.click_go_next(0)
          else:
            my_card.click_go_next(1)
          time.sleep(3)
          first = False
          if length_dict == 0:
            break


def main(fname):
  app = Application()
  app.connect(title="Yang-s6")
  dlg = app.Yangs6
  my_card = MyCard(dlg)
  res_dict = load_dict(fname)
  betting(my_card, res_dict)

if __name__ == '__main__':
  fname = 'result/1708/19.pkl'
  main(fname)
  




#app.Yangs6.ClickInput(coords=(260, 490))


