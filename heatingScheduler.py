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

    def __init__(self, instruction):
        '''
        '''
        pass

class scheduler(object):
    ''' Scheduler object to check what heating is required and when.
    '''

    def __init__(self, scheduleXMLfile):
        '''
        '''
        self.tree = ET.parse(scheduleXMLfile)
        self.root = tree.getroot()
        self.parse(self.root)

    def parse(self, XML):
        ''' Goes through the ET object and creates a list of days which
            contains 7 elements (Mon, Tues, Wed ....). Each elemtn is an 
            event object, which can be later used to check time/temps etc.
        '''
        self.days = []
        for day in XML:
            events = []
            for instruction in day:
                events.append(event(instruction))
            
            self.days.append(events)

    def fileChanged(self):
        ''' Used to check if XML schdule file has chagned since last parsed.
        '''
        #check if file changed
        #yes, re-parse and update object with new informaton
        #no, exit wihtout change
        pass

    def check(self, now):
        ''' Check if heat is required, if so what temperature.
        '''
        self.fileChanged()
        day = now.getdotw() ###
        time = now.gettime() ###
        for each in self.events(day):
            if each.start < time < each.stop:
                return True, event.temp
        else:
            return False

def checkTemp():
    '''
    '''
    pass

def heatingOn():
    ''' Sends ON command to Arduino mini to turn heating on. The ON command 
        needs to be resent periodically, but this is handled by the arduino.
    '''

def heatingOff():
    ''' Sends OFF command to Arduino mini to turn heating off. The OFF command
        needs to be resent periodically, but this is handled by the arduino.
    '''
    pass

def run(scheduleXMLfile, debug=False):
    ''' Main loop which checks the schedule to see if heating is required and
        what temperature is required. 
        
        * Schedule data comes from an XML file
        * Temperature from a database (5 minute average)
        * Boiler turned on by issuing a command to an Arduino Pro mini that
          can replay ON/OFF command of boilers OEM thermostat.
    '''
    
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
        
        time.sleep(15) # Temperature average doesn't change in less than 60
                       # seconds, so no need to run too often.

if __name__ == '__main__':
    run(SCHEDULE, DEBUG)
