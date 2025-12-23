# utils.py

import logging
from logging_config import setup_logging

setup_logging()

def log_info(message):
    logging.info(message)

    def log_error(message):
        logging.error(message)
        