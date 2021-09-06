import unittest
from LF8.src.monitor import OperatingGrade
from LF8.src.Alarmsystem import Alarmsystem
from LF8.src.main import configLog

USEDMEMORY_SOFT_LIMIT = 70.0
USEDMEMORY_HARD_LIMIT = 90.0
CPUFREQUENCY_SOFT_LIMIT = 70.0
CPUFREQUENCY_HARD_LIMIT = 90.0
alarmSystem = Alarmsystem()
operatingGrade = OperatingGrade()


def searchStringInLogfile(file_name, string_to_search):
    file_name = 'LF8/src/output/LF8.log'
    line_number = 0
    list_of_results = []
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if string_to_search in line:
                list_of_results.append((line_number, line.rstrip()))
                print(list_of_results)
                return list_of_results


class UsedMemoryTest(unittest.TestCase):
    def testDebugMode(self):
        alarmSystem.examine('Used Memory', operatingGrade.usedMemory, USEDMEMORY_SOFT_LIMIT, USEDMEMORY_HARD_LIMIT,
                            'debug', configLog())
        self.assertEqual(searchStringInLogfile('', operatingGrade.usedMemory),
                         'EXCEEDS SOFT LIMIT OF')

    @staticmethod
    def testWarningMode():
        alarmSystem.examine('Used Memory', operatingGrade.usedMemory, USEDMEMORY_SOFT_LIMIT, USEDMEMORY_HARD_LIMIT,
                            'warning', configLog())
        searchStringInLogfile('', operatingGrade.usedMemory)


class CpuFrequencyTest(unittest.TestCase):
    @staticmethod
    def testDebugMode():
        alarmSystem.examine('CPU Frequency', operatingGrade.cpuFrequency, CPUFREQUENCY_SOFT_LIMIT,
                            CPUFREQUENCY_HARD_LIMIT,
                            'debug', configLog())
        searchStringInLogfile('', operatingGrade.cpuFrequency)

    @staticmethod
    def testWaningMode(self):
        alarmSystem.examine('CPU Frequency', operatingGrade.cpuFrequency, CPUFREQUENCY_SOFT_LIMIT,
                            CPUFREQUENCY_HARD_LIMIT,
                            'warning', configLog())
        searchStringInLogfile('', operatingGrade.cpuFrequency)


if __name__ == '__main__':
    unittest.main()
