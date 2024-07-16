import os 
import sys
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
import pandas as pd

@dataclass
class ingestionConfig:
    train_data_path:str=os.path.join('Artifacts',"train.csv")
    test_data_path:str=os.path.join('Artifacts',"test.csv")
    original_data_path:str=os.path.join('Artifacts',"original.csv")

class ingestionmain:
    def __init__(self):
        self.ingestion_path=ingestionConfig()
   

    def splitting_data(self):
        logging.info("Ingestion Started")
        try:
            df=pd.read_csv('projectfolder_Calories/datasets/calories.csv')
            logging.info("Read the Dataset")
            
            
            #Creating Train.csv Folder in directory
            os.makedirs(os.path.dirname(self.ingestion_path.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_path.original_data_path,index=False,header=True)
            
            logging.info("Train Test Split performed")
            
            train_df,test_df=train_test_split(df,test_size=0.2,random_state=33)
            train_df.to_csv(self.ingestion_path.train_data_path,index=False,header=True)
            test_df.to_csv(self.ingestion_path.test_data_path,index=False,header=True)
            logging.info("Stored Train and Test dataset Respectively")
            return(
                self.ingestion_path.test_data_path,
                self.ingestion_path.train_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=ingestionmain()
    test_data,train_data=obj.splitting_data()
        
        