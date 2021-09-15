import psutil


def calculateMemory():
    return round(psutil.virtual_memory().used / (psutil.virtual_memory().total / 100), 2)


def calculateCPU():
    return round(psutil.cpu_freq().current / (psutil.cpu_freq().max / 100), 2)


class OperatingGrade:
    def __init__(self):
        self.cpuFrequency = calculateCPU()
        self.usedMemory = calculateMemory()