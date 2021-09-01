import os
from Logging import Logging


class Alarmsystem:
    parameter_label: str
    parameter_value: float
    soft_limit: float
    hard_limit: float
    logging_level = None

    def __init__(self, parameter_label, parameter_value, soft_limit, hard_limit, logging_level=None):
        self.parameter_label = parameter_label
        self.parameter_value = parameter_value
        self.soft_limit = soft_limit
        self.hard_limit = hard_limit
        self.logging_level = logging_level

    DEFAULT_PATH: str = os.path.dirname(os.path.abspath(__file__))
    APP_NAME: str = 'LF8'
    PATH_TO_LOGFILE = os.path.join(DEFAULT_PATH, APP_NAME + '.log')

    logging = Logging(PATH_TO_LOGFILE, 'debug')

    logging.logger.debug(PATH_TO_LOGFILE)
    logging.logger.debug('This is a logging test.')
