#!/usr/bin/python3

import unittest
from monitor import OperatingGrade
from Alarmsystem import Alarmsystem
from main import configLog

USEDMEMORY_SOFT_LIMIT = 50.0
USEDMEMORY_HARD_LIMIT = 90.0
CPUFREQUENCY_SOFT_LIMIT = 50.0
CPUFREQUENCY_HARD_LIMIT = 90.0
alarmSystem = Alarmsystem()
operatingGrade = OperatingGrade()


def searchStringInLogfile(stringToSearch, secondString=None):
    file_name = 'output/LF8.log'
    with open(file_name, 'r') as logFile:
        lines = logFile.readlines()
        lastMessage = lines[-1]
        if stringToSearch in lastMessage and secondString in lastMessage:
            print(lastMessage)
            return True
        else:
            print(lastMessage)
            return False


class UsedMemoryTests(unittest.TestCase):
    def testUsedMemoryDebugMode(self):
        alarmSystem.examine('Used Memory', operatingGrade.usedMemory, USEDMEMORY_SOFT_LIMIT, USEDMEMORY_HARD_LIMIT,
                            'debug', configLog())
        assert searchStringInLogfile('Used Memory', 'DEBUG') == True

    def testUsedMemoryWarningMode(self):
        alarmSystem.examine('Used Memory', operatingGrade.usedMemory, USEDMEMORY_SOFT_LIMIT, USEDMEMORY_HARD_LIMIT,
                            'warning', configLog())
        assert searchStringInLogfile('Used Memory', 'WARNING') == False


class CpuFrequencyTests(unittest.TestCase):
    def testCpuFrequencyDebugMode(self):
        alarmSystem.examine('CPU Frequency', operatingGrade.cpuFrequency, CPUFREQUENCY_SOFT_LIMIT,
                            CPUFREQUENCY_HARD_LIMIT,
                            'debug', configLog())
        assert searchStringInLogfile('CPU Frequency', 'DEBUG') == False

    def testCpuFrequencyWaningMode(self):
        alarmSystem.examine('CPU Frequency', operatingGrade.cpuFrequency, CPUFREQUENCY_SOFT_LIMIT,
                            CPUFREQUENCY_HARD_LIMIT,
                            'warning', configLog())
        assert searchStringInLogfile('CPU Frequency', 'WARNING') == True


if __name__ == '__main__':
    unittest.main()
