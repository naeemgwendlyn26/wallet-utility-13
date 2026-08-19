import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='wallet_utility.log', max_bytes=5*1024*1024, backup_count=5):
    # Create a logger
    logger = logging.getLogger('wallet_utility')
    logger.setLevel(logging.DEBUG)  # Set log level

    # Create a rotating file handler
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example Usage
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up and running.')