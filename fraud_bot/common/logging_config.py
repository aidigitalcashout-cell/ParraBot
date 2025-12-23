# logging_config.py

import logging

def setup_logging():
    logging.basicConfig(
            level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=[
                                        logging.FileHandler('fraud_bot.log'),
                                                    logging.StreamHandler()
                                                            ]
                                                                )
    