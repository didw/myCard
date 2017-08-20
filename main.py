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

def similar_prev_mid(prev_cand, prev_value, cand, value):
  if prev_value != value:
    return False
  if prev_cand[0] != cand[0] or prev_cand[2] != cand[2]:
    return False
  return True

def similar_prev_last(prev_cand, prev_value, cand, value):
  if prev_value != value:
    return False
  if prev_cand[0] != cand[0] or prev_cand[1] != cand[1]:
    return False
  return True

def betting(my_card, res_dict):
  # Bet sat first
  first = True
  for Day in ['Sat', 'Sun']:
    print("=== SAT ===")
    for rcno in range(1, 16):
      print("=== rcno: %d ===" % rcno)
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
      prev_cand = (0, 0, 0)
      prev_value = 0
      for cand, value in sorted(rc_dict.items()):
        print(cand, value)
        # if similar with previous bet just click last cand
        if similar_prev_mid(prev_cand, prev_value, cand, value):
          my_card.click_hrno(3, cand[1])
        elif similar_prev_last(prev_cand, prev_value, cand, value):
          my_card.click_hrno(4, cand[2])
        else:
          if head > 3:
            head = 1
            my_card.click_buy()
            time.sleep(3)
            my_card.click_go_next(0)
            time.sleep(3)
          my_card.click_head(head)
          my_card.click_ss()
          for j in range(3):
            my_card.click_hrno(j, cand[j])
          my_card.click_bet_total(value/100)
          head += 1
        prev_cand = cand
        prev_value = value
        # if fully betted go next
        length_dict -= 1
        if length_dict == 0:
          head = 1
          my_card.click_buy()
          time.sleep(3)
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
  from pywinauto.timings import TimeConfig
  time_config = TimeConfig()
  time_config.Fast()
  betting(my_card, res_dict)


if __name__ == '__main__':
  fname = 'result/1708/19.pkl'
  main(fname)
  




#app.Yangs6.ClickInput(coords=(260, 490))


