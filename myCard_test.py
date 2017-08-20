#!/usr/bin/python
# -*- coding: utf-8 -*-
from myCard import *


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


