#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ciarán Mooney 2017
# contact@cmooney.co.uk
# Tests for heating-scheduler.

import unittest
from unittest import mock

import heatingScheduler

class example(unittest.TestCase):
    '''
    '''

    def setUp(self):
        '''
        '''
        pass

    def text_example(self):
        '''
        '''

class TestRun(unittest.TestCase):
    ''' Tests the run function defined in heatingSchedule
    '''

    def setUp(self):
        '''
        '''

        self.XML = "test-data/schedule-1.xml"

    def test_scheduler_init(self):
        ''' Test that when run(self.XML) called that a scheduler object is 
            created.
        '''
        self.assertTrue(False)

    def test_scheduler_xml_error(self):
        ''' Test that when run(self.XML) called with a bad XML file that it
            produces the correct error.
        '''
        self.assertTrue(False)

    def test_scheduler_heatingNotRequired(self):
        ''' Checks that the heatingOff function is called.
        '''
        self.assertTrue(False)

    def test_scheduler_heatingRequiredTempLow(self):
        ''' Checks that the loop calls the heatingOn() function. 
        '''
        self.assertTrue(False)

    def test_scheduler_heatingRequiredTempCorrect(self):
        ''' Checks that the loop calls the HeatingOff() function.
        '''
        self.assertTrue(False)

    def test_scheduler_heatingRequiredTempHigh(self):
        ''' Checks that the loop calls the HeatingOff() function.
        '''
        self.assertTrue(False)

    def test_scheduler_recallafter15seconds(self):
        ''' Checks that the loop re-runs after 15 seconds
        '''
        self.assertTrue(False)
    
    def test_scheduler_checkXMLfilechange(self):
        ''' Checks that after an xml file change that the changes "take".
        '''
        self.assertTrue(False)


if __name__ == '__main__':
        unittest.main(verbosity=2)
