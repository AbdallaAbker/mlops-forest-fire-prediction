import os 
import sys
import logging
from datetime import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(filename)s: %(module)s: %(message)s]"
log_dir= "logs"
datetime_str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
log_file_name = f"{datetime_str} + _fire_forest_prediction.log"
log_filepath = os.path.join(log_dir, log_file_name)
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(level=logging.INFO, 
                    format = logging_str,

                    handlers=[
                        logging.FileHandler(log_filepath), #to create a log file
                        logging.StreamHandler(sys.stdout) #to show logs on terminal
                    ]
                )

logger = logging.getLogger("fire_forest_predictionLogger")


