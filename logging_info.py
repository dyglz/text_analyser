
import logging

class LoggingInfo:

    @staticmethod
    def configure_logging():
        logging.basicConfig(
            level=logging.INFO,
            filename="text_analyser_log.txt",
            filemode="a",
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    @staticmethod
    def log_info(message:str) -> None:
        logging.info(message)
    
    @staticmethod
    def log_warning(message: str) -> None:
        logging.warning(message)
        
    @staticmethod
    def log_error(message:str) -> None:
        logging.error(message)
    
    @staticmethod
    def log_critical(message: str) -> None:
        logging.critical(message)
