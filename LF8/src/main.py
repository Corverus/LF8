#!/usr/bin/python3

import logging
import os
import sys
import Alarmsystem
import monitor


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
            Alarmsystem.Alarmsystem.examine('CPU Frequency', monitor.OperatingGrade().cpuFrequency, 70, 90,
                                            'debug', configLog())
        elif argument == '-memory':
            Alarmsystem.Alarmsystem.examine('Used Memory', monitor.OperatingGrade().usedMemory, 70, 90,
                                            'debug', configLog())
        else:
            print('Wrong Input\nTry -h or --help for more information.')
    else:
        Alarmsystem.Alarmsystem.examine('CPU Frequency', monitor.OperatingGrade().cpuFrequency, 70, 90,
                                        'debug', configLog())
        print('')
        Alarmsystem.Alarmsystem.examine('Used Memory', monitor.OperatingGrade().usedMemory, 70, 90,
                                        'debug', configLog())


useArguments()
