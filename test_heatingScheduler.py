#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Ciarán Mooney 2017
# contact@cmooney.co.uk
# Tests for heating-scheduler.

import unittest
import unittest.mock as mock
import heatingScheduler

class ErrorAfter(object):
    '''
    Callable that will raise `CallableExhausted`
    exception after `limit` calls

    '''
    def __init__(self, limit):
        self.limit = limit
        self.calls = 0

    def __call__(self, required, temp):
        print(required, temp)
        self.calls += 1
        if self.calls > self.limit:
            raise CallableExhausted

        return required, temp

class CallableExhausted(Exception):
    pass


class TestRun(unittest.TestCase):
    ''' Tests the run function defined in heatingSchedule
    '''

    def setUp(self):
        '''
        '''
        self.XML = 'test-data/schedule.xml'
        self.debug = True

    def test_scheduler_init(self):
        ''' Test that when run(self.XML) called that a scheduler object is 
            created.
        '''
        self.assertTrue(False)

    def test_scheduler_xml_error(self):
        ''' Test that when run(self.XML) called with a bad XML file that it
            produces the correct error.
        '''

        self.XML = 'test-data/scheduleError1.xml'
        heatingScheduler.run(self.XML)
        self.assertTrue(False)

    @mock.patch('heatingScheduler.scheduler',  
                side_effect=ErrorAfter(2), autospec=True)
    # XXX Re-write so this can only be called twice. see
    # http://igorsobreira.com/2013/03/17/testing-infinite-loops.html
    @mock.patch('heatingScheduler.heatingOn')
    @mock.patch('heatingScheduler.heatingOff')
    @mock.patch('heatingScheduler.checkTemp')
    def test_scheduler_heatingNotRequired(self, mock_checkTemp, mock_heatingOff, 
                                            mock_heatingOn, mock_scheduler):
        ''' Checks that the heatingOff function is called.
        '''
        ### Need to mock the time.sleep() function to speed things up.
        mock_scheduler.check.return_value((False, None))
        mock_checkTemp.return_value(25)
        heatingScheduler.run(self.XML, self.debug)
        self.assertFalse(mock_heatingOn.called)
        self.assertTrue(mock_heatingOff.called)
        
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
