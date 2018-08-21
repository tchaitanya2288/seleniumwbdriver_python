import logging
import logging.config

class LoggerDemoConf():

    def testLog(self):
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConf.__name__)

        #logging Messages
        logger.debug("debug messages")
        logger.info("info messages")
        logger.warning("warning messages")
        logger.error("error messages")
        logger.critical("critical messages")

demo = LoggerDemoConf()
demo.testLog()
