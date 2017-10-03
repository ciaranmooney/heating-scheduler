#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Ciarán Mooney 2017
# contact@cmooney.co.uk
# A heating controller for my home. It currently uses a hard coded XML file to
# program the schedule. It issues commands via I2C to an arduino that controls
# the boiler over 433 Mhz RF.

DEBUG = True
SCHEDULE = 'schedule.xml'

def log(message, debug):
    ''' Handy global for printing debug messages.
    '''
    if debug:
        print(message)

def run(schedule, debug):
    ''' Main loop which checks to see if a command needs to be issued.
    '''
    # check schedule
    # check temperature
    # action required
    # wait
    while True:
        heatingStatus, requiredTemp = checkSchedule(now)
        currentTemp = checkTemp()
        if heatingStatus and (currentTemp < requiredTemp):
            log("Too cool, turning heating on", debug)
            heatingOn()
        if heatingStatus and (currentTemp > requiredTemp):
            log("Too hot, turning heating on", debug)
            heatingOff()
        if heatingStatus == False:
            log("Heating off", debug)
            heatingOff()
        
        time.sleep(15)

if __name == '__main__':
    run(SCHEDULE, DEBUG)
