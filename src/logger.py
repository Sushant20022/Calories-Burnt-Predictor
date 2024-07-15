import logging
import sys 
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FOLDER=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(LOG_FOLDER,exist_ok=True)
FINAL_PATH=os.path.join(LOG_FOLDER,LOG_FILE)


logging.basicConfig(
filename=FINAL_PATH,
format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
level=logging.INFO,




)