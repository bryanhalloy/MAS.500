#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 00:01:29 2016

@author: bryanhalloy
"""

#This is a unit test for morediscussed_v03.py


import morediscussed_v03
import unittest


class GetSenCountTest(unittest.TestCase):

    def setUp(self):
        self.results = getsentencecount("clinton", key_mediacloud, datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 2))
        
    def testKeyWorks(self):
        search_count = self.results
        assert search_count > 0 


# if this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()

