import logging


def init_logger(name):
    logging.basicConfig(format="%(asctime)s %(name)s  %(levelname)s  %(message)s")
    _logger = logging.getLogger(name)
    _logger.level = logging.DEBUG
    return _logger
