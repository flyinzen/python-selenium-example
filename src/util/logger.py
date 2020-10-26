import logging

LOG_LEVEL = logging.INFO
LOG_FORMAT = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"


def get_logger(name):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(LOG_LEVEL)
    stream_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger = logging.getLogger(name)
    logger.addHandler(stream_handler)
    return logger