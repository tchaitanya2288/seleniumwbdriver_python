import logging
class Loggerdemoconsole():
    def test1(self):
        #Create logger
        logger = logging.getLogger(Loggerdemoconsole.__name__)
        logger.setLevel(logging.INFO)
        #Create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)
        #Create formatter
        formatter = logging.Formatter('%(asctime)s: -%(name)s - %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p')
        #Add formatter to console handler --> chandler
        chandler.setFormatter(formatter)
        #add console handler to logger
        logger.addHandler(chandler)

        #logging messages
        logger.debug("Debug message")
        logger.warning("warning message")
        logger.info("info message")
        logger.error("error message")
        logger.critical("critical message")

cd = Loggerdemoconsole()
cd.test1()

