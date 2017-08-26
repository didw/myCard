#!/usr/bin/python
# -*- coding: utf-8 -*-
from pywinauto.application import Application
import time
from myCard import *

coords_day = {"Sat": (260, 490), "Sun": (400, 490)}
coords_head = {1: (155, 255), 2: (260, 255), 3: (370, 255)}
coords_rcno = { 1: (90, 620),  2: (200, 620),  3: (315, 620),  4: (425, 620)
             ,  5: (90, 685),  6: (200, 685),  7: (315, 685),  8: (425, 685)
             ,  9: (90, 745), 10: (200, 745), 11: (315, 745), 12: (425, 745)
             , 13: (90, 810), 14: (200, 810), 15: (315, 810), 16: (425, 810)}

coords_hrno = [{  1:  (55, 470),  2: (113, 470),  3: (172, 470),  4: (230, 470)
               ,  5: (290, 470),  6: (348, 470),  7: (406, 470),  8: (465, 470)
               ,  9:  (55, 515), 10: (113, 515), 11: (172, 515), 12: (230, 515)
               , 13: (290, 515), 14: (348, 515), 15: (406, 515), 16: (465, 515)},
               {  1:  (55, 570),  2: (113, 570),  3: (172, 570),  4: (230, 570)
               ,  5: (290, 570),  6: (348, 570),  7: (406, 570),  8: (465, 570)
               ,  9:  (55, 615), 10: (113, 615), 11: (172, 615), 12: (230, 615)
               , 13: (290, 615), 14: (348, 615), 15: (406, 615), 16: (465, 615)},
               {  1:  (55, 670),  2: (113, 670),  3: (172, 670),  4: (230, 670)
               ,  5: (290, 670),  6: (348, 670),  7: (406, 670),  8: (465, 670)
               ,  9:  (55, 715), 10: (113, 715), 11: (172, 715), 12: (230, 715)
               , 13: (290, 715), 14: (348, 715), 15: (406, 715), 16: (465, 715)},
               {  1:  (55, 600),  2: (113, 600),  3: (172, 600),  4: (230, 600)
               ,  5: (290, 600),  6: (348, 600),  7: (406, 600),  8: (465, 600)
               ,  9:  (55, 645), 10: (113, 645), 11: (172, 645), 12: (230, 645)
               , 13: (290, 645), 14: (348, 645), 15: (406, 645), 16: (465, 645)},
               {  1:  (55, 700),  2: (113, 700),  3: (172, 700),  4: (230, 700)
               ,  5: (290, 700),  6: (348, 700),  7: (406, 700),  8: (465, 700)
               ,  9:  (55, 745), 10: (113, 745), 11: (172, 745), 12: (230, 745)
               , 13: (290, 745), 14: (348, 745), 15: (406, 745), 16: (465, 745)}]

coords_bet = [{   1:  (60, 785),    2: (128, 785),    3: (196, 785)
              ,   5: (264, 785),   10: (332, 785),   20: (400, 785),    30: (468, 785)
              ,  40:  (60, 830),   50: (128, 830),  100: (196, 830)
              , 200: (264, 830),  300: (332, 830),  500: (400, 830),  1000: (468, 830)},
              {   1:  (60, 813),    2: (128, 813),    3: (196, 813)
              ,   5: (264, 813),   10: (332, 813),   20: (400, 813),    30: (468, 813)
              ,  40:  (60, 860),   50: (128, 860),  100: (196, 860)
              , 200: (264, 860),  300: (332, 860),  500: (400, 860),  1000: (468, 860)}]

amount_list = [1, 2, 3, 5, 10, 20, 30, 40, 50, 100, 200, 300, 500, 1000]
amount_list.reverse()

class MyCard():
    def __init__(self, app):
        self.app = app
        self.first_rc = 1
        self.line_overflow = 0

    def initialize(self):
        self.line_overflow = 0

    def click_day(self, day):
        self.app.ClickInput(coords=coords_day[day])

    def click_rcno(self, rcno):
        self.app.ClickInput(coords=coords_rcno[rcno])

    def click_next(self):
        self.app.ClickInput(coords=(380, 900))

    def click_confirm(self):
        self.app.ClickInput(coords=(410, 565))

    def click_head(self, idx):
        self.app.ClickInput(coords=coords_head[idx])

    def click_ss(self):
        self.app.ClickInput(coords=(465, 344))

    def click_hrno(self, idx, hrno):
        self.app.ClickInput(coords=coords_hrno[idx][hrno])

    def click_bet_specific(self, amount):
        self.app.ClickInput(coords=coords_bet[self.line_overflow][amount])

    def click_bet_total(self, amount):
        for bet in amount_list:
            if bet <= amount:
                self.click_bet_specific(bet)
                amount -= bet
                if self.first_rc == 0:
                    self.line_overflow = 1
                if amount == 0:
                    break
        self.line_overflow = 0

    def click_buy(self, n_bet):
        self.app.ClickInput(coords=(400, 920))  # 바로구매
        self.app.ClickInput(coords=(400, 610))  # 예매 알림 확인
        if n_bet == 1:
          self.app.ClickInput(coords=(395, 670))  # 즉시구매
        elif n_bet == 2:
          self.app.ClickInput(coords=(395, 760))  # 즉시구매
        else:
          self.app.ClickInput(coords=(395, 850))  # 즉시구매
        self.initialize()

    def click_go_next(self, next):
        """next: 0 - buy next race
                 1 - buy next race again
        """
        if next == 0:
            self.app.ClickInput(coords=(265, 740))  # 동일경주구매
        else:
            self.app.ClickInput(coords=(100, 740))  # 다른경주구매
            self.first_rc = 0


class TestMyCard(MyCard):
    def __init__(self, app):
        super(TestMyCard, self).__init__(app)

    def test_click_day(self):
        """test click Sat"""
        self.click_day("Sat")

    def test_click_rcno(self):
        """test click rcno"""
        for key in sorted(coords_rcno.keys()):
            print("Click %s" % key)
            self.click_rcno(key)
            time.sleep(1)

    def test_click_hrno(self):
        """test click rcno"""
        for idx in range(3):
            for key in sorted(coords_hrno[idx].keys()):
                print("Click %s" % key)
                self.click_hrno(idx, key)
                time.sleep(1)

    def test_click_next(self):
        """test click next"""
        self.click_next()

    def test_main(self):
        self.click_day("Sun")
        self.click_rcno("4R")
        self.click_next()
        self.click_confirm()

    def test_click_bet_specific(self):
        self.first_rc = 0
        for bet in bet_list:
            self.click_bet_specific(bet)
            self.line_overflow = 1

    def test_click_bet_total(self):
        self.first_rc = 0
        self.click_bet_total(474)


if __name__ == '__main__':
    app = Application()
    app.connect(title="Yang-s6")
    dlg = app.Yangs6
    test = TestMyCard(dlg)
    #test.test_main()
    test.test_click_bet_total()



#app.Yangs6.ClickInput(coords=(260, 490))


