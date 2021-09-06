#!/usr/bin/python3

import logging
import os
from Alarmsystem import Alarmsystem


def configLog():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
        filename=os.path.join('output', 'LF8.log')
    )
    return logging.getLogger()


Alarmsystem.examine('testparameter', 6, 3, 5, 'debug', configLog())
