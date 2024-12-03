# creatting custom logging 
import os 
import sys
import logging 

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # how the logging string should looks like 

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")

os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(level = logging.INFO, format=logging_str, handlers=[
    logging.FileHandler(log_filepath),
    logging.StreamHandler(sys.stdout) # to see the output in terminal 
])
logger= logging.getLogger("projectLogger")