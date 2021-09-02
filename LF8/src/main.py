#!/usr/bin/python3

import logging
import os
from Alarmsystem import Alarmsystem

DEFAULT_PATH: str = os.path.dirname(os.path.abspath(__file__))
APP_NAME: str = 'LF8'
PATH_TO_LOGFILE = os.path.join(DEFAULT_PATH, APP_NAME + '.log')

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    filename=PATH_TO_LOGFILE
)
logger = logging.getLogger()

Alarmsystem.examine('testparameter', 6, 3, 5, 'debug', logger)
