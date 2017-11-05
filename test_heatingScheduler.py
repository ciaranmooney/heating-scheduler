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
    def __init__(self, limit, heat, temp):
        self.limit = limit
        self.calls = 0
        self.heat = heat
        self.temp = temp

    def __call__(self, now):
        self.calls += 1
        if self.calls > self.limit:
            raise CallableExhausted

        return self.heat, self.temp

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
    
    @mock.patch('time.sleep') # Simple mock to speed up tests, don't actually
                              # need to use it.
    @mock.patch('heatingScheduler.heatingOn')
    @mock.patch('heatingScheduler.heatingOff')
    @mock.patch('heatingScheduler.scheduler.check',  
                side_effect=ErrorAfter(2, False, 25))
    @mock.patch('heatingScheduler.checkTemp')
    def test_scheduler_heatingNotRequired(self, mock_checkTemp, mock_scheduler,
                                            mock_heatingOff, mock_heatingOn,
                                            mock_timesleep):
        ''' Checks that the heatingOff function is called.
        '''
        mock_checkTemp.return_value(25)
        try:
            heatingScheduler.run(self.XML, self.debug)
        except CallableExhausted:
            # To catch the error thrown by the second loop, see errorAfter()
            pass

        self.assertFalse(mock_heatingOn.called)
        self.assertTrue(mock_heatingOff.called)
       

    @mock.patch('time.sleep') # Simple mock to speed up tests, don't actually
                              # need to use it.
    @mock.patch('heatingScheduler.heatingOn')
    @mock.patch('heatingScheduler.heatingOff')
    @mock.patch('heatingScheduler.scheduler.check',  
                side_effect=ErrorAfter(2, True, 25))
    @mock.patch('heatingScheduler.checkTemp', return_value=20)
    def test_scheduler_heatingRequiredTempLow(self, mock_checkTemp, mock_scheduler,
                                                mock_heatingOff,  mock_heatingOn,
                                                mock_timesleep):
        ''' Checks that the loop calls the heatingOn() function. 
        '''
        try:
            heatingScheduler.run(self.XML, self.debug)
        except CallableExhausted:
            # To catch the error thrown by the second loop, see errorAfter()
            pass

        self.assertTrue(mock_heatingOn.called)
        self.assertFalse(mock_heatingOff.called)

    
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
