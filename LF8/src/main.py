#!/usr/bin/python3

import logging
import os
import sys
import Alarmsystem
import monitor
import logInDienst

alarmSystem = Alarmsystem.Alarmsystem
monitor = monitor.OperatingGrade
SOFT_LIMIT = 70
HARD_LIMIT = 90


def configLog():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
        filename=os.path.join('../src/output', 'LF8.log'),
        force=True
    )
    return logging.getLogger()


def useArguments():
    if len(sys.argv) == 2:
        argument = sys.argv[1]
        if argument == '-h' or argument == '--help':
            print('-cpu -> CPU-Frequency\n-memory -> utilized Memory')
        elif argument == '-cpu':
            alarmSystem.examine('CPU Frequency', 91, SOFT_LIMIT, HARD_LIMIT, 'debug', configLog())
        elif argument == '-memory':
            alarmSystem.examine('Used Memory', monitor().usedMemory, SOFT_LIMIT, HARD_LIMIT, 'debug', configLog())
        else:
            print('Wrong Input\nTry -h or --help for more information.')
    else:
        alarmSystem.examine('CPU Frequency', monitor().cpuFrequency, SOFT_LIMIT, HARD_LIMIT, 'warning', configLog())
        print('')
        alarmSystem.examine('Used Memory', monitor().usedMemory, SOFT_LIMIT, HARD_LIMIT, 'debug', configLog())

AcountManager = logInDienst.LogInService()
useArguments()
