import os
import sys
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.Data_Transformation import Transformer


@dataclass
class IngestionConfig:
    train_data_path: str = os.path.join('Artifacts', "train.csv")
    test_data_path: str = os.path.join('Artifacts', "test.csv")
    original_data_path: str = os.path.join('Artifacts', "original.csv")

class IngestionMain:
    def __init__(self):
        self.ingestion_path = IngestionConfig()

    def splitting_data(self):
        logging.info("Ingestion Started")
        try:
            df = pd.read_csv('projectfolder_Calories/data/dataset.csv')
            logging.info("Read the Dataset")

            logging.info(f"Dataset columns: {df.columns.tolist()}")

            # Creating Train.csv Folder in directory
            os.makedirs(os.path.dirname(self.ingestion_path.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_path.original_data_path, index=False, header=True)
            
            logging.info("Train Test Split performed")
            
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=33)
            train_df.to_csv(self.ingestion_path.train_data_path, index=False, header=True)
            test_df.to_csv(self.ingestion_path.test_data_path, index=False, header=True)
            logging.info("Stored Train and Test dataset respectively")
            return (
                self.ingestion_path.test_data_path,
                self.ingestion_path.train_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = IngestionMain()
    test_data, train_data = obj.splitting_data()

    data_transformation = Transformer()
    train_arr, test_arr, _ = data_transformation.start_transformation(train_data, test_data)
