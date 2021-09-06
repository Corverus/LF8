#!/usr/bin/python3

import logging
import os
from Alarmsystem import Alarmsystem

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    filename=os.path.join('output', 'LF8.log')
    # filename='LF8.log'
)
logger = logging.getLogger()
Alarmsystem.examine('testparameter', 6, 3, 5, 'debug', logger)
