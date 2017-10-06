#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Ciarán Mooney 2017
# contact@cmooney.co.uk
# A heating controller for my home. It currently uses a hard coded XML file to
# program the schedule. It issues commands via I2C to an arduino that controls
# the boiler over 433 Mhz RF.

DEBUG = True
SCHEDULE = 'schedule.xml'

from datetime import datetime
import xml.etree.ElementTree as ET
import os

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

class scheduler(object):
    '''
    '''

    def __init__(self, scheduleXMLfile):
        '''
        '''
        self.tree = ET.parse(scheduleXMLfile)
        self.root = tree.getroot()
        self.parse(self.root)

    def parse(self, XML):
        '''
        '''
        self.events = []
        for day in XML:
            events = []
            for instruction in day:
                events.append(event(instruction)) 
            
            self.events.append(events)

    def fileChanged(self):
        '''
        '''
        #check if file changed
        #yes, re-parse and update object with new informaton
        #no, exit wihtout change
        pass

    def check(self, now)
        '''
        '''
        self.fileChanged()
        day = now.getdotw() ###
        time = now.gettime() ###
        for each in self.events(day):
            if each.start < time < each.stop:
                return True, event.temp

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

def run(scheduleXMLfile, debug):
    ''' Main loop which checks to see if a command needs to be issued.
    '''
    # check schedule
    # check temperature
    # action required
    # wait
    schedule = scheduler(scheduleXMLfile)
    while True:
        now = datetime.now()
        heatingRequired, requiredTemp = schedule.check(now)
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
