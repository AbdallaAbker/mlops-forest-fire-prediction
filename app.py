from src.logging import logger
from src.exception import CustomException
import sys


if __name__ == "__main__":
    logger.info("Started")

    try:
       a = 1/0
    except Exception as e:
        logger.info(f"{e}")
        raise CustomException(e, sys)
        
