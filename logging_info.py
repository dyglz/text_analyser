import logging

class LoggingInfo:

    def configure_logging():
        logging.basicConfig(
            level=logging.DEBUG,
            filename="text_analyser_log.txt",
            filemode="a",
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    
    def log_debug(message):
        logging.debug(message)
    
    def log_info(message):
        logging.info(message)
    
    def log_warning(message):
        logging.warning(message)
    
    def log_error(message):
        logging.error(message)
    
    def log_critical(message):
        logging.critical(message)