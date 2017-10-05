#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Ciarán Mooney 2017
# contact@cmooney.co.uk
# A heating controller for my home. It currently uses a hard coded XML file to
# program the schedule. It issues commands via I2C to an arduino that controls
# the boiler over 433 Mhz RF.
#
DEBUG = True
SCHEDULE = 'schedule.xml'

from datetime import datetime
import xml.etree.ElementTree as ET

def log(message, debug):
    ''' Handy global for printing debug messages.
    '''
    if debug:
        print(message)

class event(object):
    '''
    '''

    def __init__(self):
        '''
        '''
        pass

def checkSchedule(now, schedule):
    ''' Checks the schedule to see if heaing is required and if so what
        temperature.
    '''
    dotw = datetime.weekday(now)
    time = datetime.time(now)
    
    tree = ET.parse('schedule')
    root = tree.getroot()
    events = root[dotw]
    
    return heat, temperature

def checkTemp():
    '''
    '''
    pass

def heatingOn():
    '''
    '''

def heatingOff():
    '''
    '''
    pass

def run(schedule, debug):
    ''' Main loop which checks to see if a command needs to be issued.
    '''
    # check schedule
    # check temperature
    # action required
    # wait
    while True:
        now = datetime.now
        heatingRequired, requiredTemp = checkSchedule(now, schedule)
        currentTemp = checkTemp()
        if heatingRequired and (currentTemp < requiredTemp):
            log("Too cool, turning heating on", debug)
            heatingOn()
        if heatingRequired and (currentTemp > requiredTemp):
            log("Too hot, turning heating off", debug)
            heatingOff()
        if heatingRequired == False:
            log("Heating off", debug)
            heatingOff()
        
        time.sleep(15)

if __name == '__main__':
    run(SCHEDULE, DEBUG)
