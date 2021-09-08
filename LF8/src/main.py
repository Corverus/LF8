#!/usr/bin/python3

import logging
import os


def configLog():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
        filename=os.path.join('output', 'LF8.log'),
        force=True
    )
    return logging.getLogger()
