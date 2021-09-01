import psutil
import alert


def calculateMemory():
    return psutil.virtual_memory().used


def calculateCPU():
    return psutil.cpu_freq().current / (psutil.cpu_freq().max / 100)


class OperatingGrade:
    def __init__(self):
        self.cpuFrequency = calculateCPU()
        self.usedMemory = calculateMemory()
