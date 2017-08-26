#!/usr/bin/python
# -*- coding: utf-8 -*-
from myCard import *
import json
import pickle
import os


def verify_bet_list(bet_list):
  for day in ['Sat', 'Sun']:
    bet_list_day = bet_list[day]
    for rcno in range(1, 16):
      if rcno not in bet_list_day:
        continue
      bet_rc = bet_list_day[rcno]
      for target in bet_rc:
        print("Day: %s, rcno: %d, target: %d, %d, %d,  value: %d" %
              (day, rcno, target[0], target[1], target[2], bet_rc[target]))


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

def save_dict(data, fname):
  return pickle.dump(data, open(fname, 'wb'))

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

def betting(my_card, res_dict, is_done, f_done):
  # Bet sat first
  first = True
  first = False
  for Day in ['Sun']:
    print("=== SAT ===")
    for rcno in range(1, 16):
      if rcno in is_done[Day] and is_done[Day][rcno][-1] == 1:
        print("%s: %d is bet already. pass.." % (Day, rcno))
        continue
      if rcno not in res_dict[Day]:
        continue
      print("=== rcno: %d ===" % rcno)
      if rcno not in is_done[Day]:
        is_done[Day][rcno] = [0]*500
      rc_dict = res_dict[Day][rcno]
      length_dict = len(rc_dict)
      if length_dict == 0:
        continue
      my_card.click_day(Day)
      my_card.click_day(Day)
      my_card.click_rcno(rcno)
      my_card.click_rcno(rcno)
      my_card.click_next()
      if not first:
        my_card.click_confirm()
      time.sleep(2)
      head = 1
      prev_cand = (0, 0, 0)
      prev_value = 0
      i_b = 0
      for cand, value in sorted(rc_dict.items()):
        ## Missing Horse
        if rcno == 4 and 11 in cand:
          print("[%d] %s:%d[%d] is missing. pass.." % (i_b, Day, rcno, i_b))
          is_done[Day][rcno][i_b] = 1
          i_b += 1
          length_dict -= 1
          continue
        ############

        if is_done[Day][rcno][i_b] == 1:
          print("[%d] %s:%d[%d] is bet already. pass.." % (i_b, Day, rcno, i_b))
          i_b += 1
          length_dict -= 1
          continue
        print(i_b, cand, value, length_dict)
        # if similar with previous bet just click last cand
        if similar_prev_mid(prev_cand, prev_value, cand, value):
          if my_card.first_rc == 1 and Day == 'Sat':
            my_card.click_hrno(1, cand[1])
          else:
            my_card.click_hrno(3, cand[1])
          is_done[Day][rcno][i_b] = 1
          i_b += 1
        elif similar_prev_last(prev_cand, prev_value, cand, value):
          if my_card.first_rc == 1 and Day == 'Sat':
            my_card.click_hrno(2, cand[2])
          else:
            my_card.click_hrno(4, cand[2])
          is_done[Day][rcno][i_b] = 1
          i_b += 1
        else:
          if head > 3:
            head = 1
            my_card.click_buy(3)
            time.sleep(3)
            my_card.click_go_next(0)
            time.sleep(3)
          if head == 1:
            time.sleep(1)
          if head != 1:
            time.sleep(1)
            my_card.click_head(head)
            time.sleep(1)
          my_card.click_ss()
          for j in range(3):
            my_card.click_hrno(j, cand[j])
          my_card.click_bet_total(value/100)
          head += 1
          is_done[Day][rcno][i_b] = 1
          i_b += 1
          save_dict(is_done, f_done)
        prev_cand = cand
        prev_value = value
        # if fully betted go next
        length_dict -= 1
        if length_dict == 0:
          my_card.click_buy(head-1)
          time.sleep(3)
          my_card.click_go_next(1)
          time.sleep(3)
          first = False
          head = 1
          break
      is_done[Day][rcno][-1] = 1
      save_dict(is_done, f_done)
    is_done[Day] = 1
    save_dict(is_done, f_done)


def main(fname):
  app = Application()
  app.connect(title="Yang-s6")
  dlg = app.Yangs6
  my_card = MyCard(dlg)
  res_dict = load_dict(fname)
  from pywinauto.timings import TimeConfig
  time_config = TimeConfig()
  time_config.Fast()
  is_done = {'Sat':{}, 'Sun':{}}
  f_done = fname.replace('.pkl', '_done.pkl')
  if os.path.exists(f_done):
    is_done = load_dict(f_done)
  # Personal setting..
  my_card.first_rc = 0
  for i in range(1, 6):
    is_done['Sun'][i] = [1]*500
  is_done['Sun'][6] = [0]*500
  for i in range(216):
    is_done['Sun'][6][i] = 1
  for i in range(216, 500):
    is_done['Sun'][6][i] = 0

  betting(my_card, res_dict, is_done, f_done)


if __name__ == '__main__':
  fname = '../kra/result/1708/26.pkl'
  main(fname)
  




#app.Yangs6.ClickInput(coords=(260, 490))


