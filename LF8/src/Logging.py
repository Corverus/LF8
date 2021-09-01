#!/usr/bin/python3

import logging


class Logging:

    logger = None

    def __init__(self, path_to_logfile, log_level):
        if log_level == 'warning':
            level = logging.WARNING
        else:
            level = logging.DEBUG

        logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=level,
            filename=path_to_logfile,
            filemode='w'
        )
        self.logger = logging.getLogger()
