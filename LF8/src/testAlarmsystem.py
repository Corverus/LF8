#!/usr/bin/python3

import unittest
from Alarmsystem import Alarmsystem
from main import configLog

FIXMEMORY = 80.20
FIXCPU = 40.20
USEDMEMORY_SOFT_LIMIT = 50.0
USEDMEMORY_HARD_LIMIT = 90.0
CPUFREQUENCY_SOFT_LIMIT = 50.0
CPUFREQUENCY_HARD_LIMIT = 90.0
alarmSystem = Alarmsystem()


def searchStringInLogfile(stringToSearch, secondString=None):
    file_name = 'output/LF8.log'
    with open(file_name, 'r') as logFile:
        lines = logFile.readlines()
        lastMessage = lines[-1]
        print(lastMessage)
        if stringToSearch in lastMessage and secondString in lastMessage:
            return True
        else:
            return False


class UsedMemoryTests(unittest.TestCase):
    def testUsedMemoryDebugMode(self):
        alarmSystem.examine('Used Memory', FIXMEMORY, USEDMEMORY_SOFT_LIMIT, USEDMEMORY_HARD_LIMIT,
                            'debug', configLog())
        assert searchStringInLogfile('WARNING', 'SOFT LIMIT') == True

    def testUsedMemoryWarningMode(self):
        alarmSystem.examine('Used Memory', FIXMEMORY + 10, USEDMEMORY_SOFT_LIMIT, USEDMEMORY_HARD_LIMIT,
                            'warning', configLog())
        assert searchStringInLogfile('WARNING', 'HARD LIMIT') == True


class CpuFrequencyTests(unittest.TestCase):
    def testCpuFrequencyDebugMode(self):
        alarmSystem.examine('CPU Frequency', FIXCPU, CPUFREQUENCY_SOFT_LIMIT,
                            CPUFREQUENCY_HARD_LIMIT,
                            'debug', configLog())
        assert searchStringInLogfile('DEBUG', 'SOFT LIMIT') == False

    def testCpuFrequencyWaningMode(self):
        alarmSystem.examine('CPU Frequency', FIXCPU + 10, CPUFREQUENCY_SOFT_LIMIT,
                            CPUFREQUENCY_HARD_LIMIT,
                            'warning', configLog())
        assert searchStringInLogfile('WARNING', 'SOFT LIMIT') == True


if __name__ == '__main__':
    unittest.main()
