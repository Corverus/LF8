import unittest
from monitor import OperatingGrade
from Alarmsystem import Alarmsystem
from main import configLog

USEDMEMORY_SOFT_LIMIT = 70.0
USEDMEMORY_HARD_LIMIT = 90.0
CPUFREQUENCY_SOFT_LIMIT = 70.0
CPUFREQUENCY_HARD_LIMIT = 90.0
alarmSystem = Alarmsystem()
operatingGrade = OperatingGrade()


def searchStringInLogfile(string_to_search):
    file_name = 'output/LF8.log'
    with open(file_name, 'r') as logFile:
        lines = logFile.readlines()
        lastMessage = lines[-1]
        if string_to_search in lastMessage:
            print(lastMessage)
            return True
        else:
            return False


class UsedMemoryTests(unittest.TestCase):
    def testDebugMode(self):
        alarmSystem.examine('Used Memory', operatingGrade.usedMemory, USEDMEMORY_SOFT_LIMIT, USEDMEMORY_HARD_LIMIT,
                            'debug', configLog())
        assert searchStringInLogfile('USED MEMORY') == True


    def testWarningMode(self):
        alarmSystem.examine('Used Memory', operatingGrade.usedMemory, USEDMEMORY_SOFT_LIMIT, USEDMEMORY_HARD_LIMIT,
                            'warning', configLog())
        assert searchStringInLogfile('USED MEMORY') == True


class CpuFrequencyTest(unittest.TestCase):
    def testDebugMode(self):
        alarmSystem.examine('CPU Frequency', operatingGrade.cpuFrequency, CPUFREQUENCY_SOFT_LIMIT,
                            CPUFREQUENCY_HARD_LIMIT,
                            'debug', configLog())
        assert searchStringInLogfile('CPU FREQUENCY') == True

    def testWaningMode(self):
        alarmSystem.examine('CPU Frequency', operatingGrade.cpuFrequency, CPUFREQUENCY_SOFT_LIMIT,
                            CPUFREQUENCY_HARD_LIMIT,
                            'warning', configLog())
        assert searchStringInLogfile('CPU FREQUENCY') == True


if __name__ == '__main__':
    unittest.main()
