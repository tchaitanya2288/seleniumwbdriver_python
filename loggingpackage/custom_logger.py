import inspect
import logging

def customLogger(logLevel):

    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    #By default log all messages
    logger.setLevel(logging.DEBUG)

    filehandler = logging.FileHandler("{0}.log".format(loggerName), mode='w')
    filehandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s: -%(name)s:- %(levelname)s: %(message)s',datefmt='%m%d%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger


