import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.utils import save_object
from src.logger import logging
from src.exception import CustomException

@dataclass
class TransformationConfig:
    preprocess_obj_path: str = os.path.join("Artifacts", "preprocessor.pkl")

class Transformer:
    def __init__(self):
        self.obj_path = TransformationConfig()

    def TransformerFunction(self):
        try:
            numerical_columns = ['Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
            categorical_columns = ['Gender']
            
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            num_pipeline = Pipeline(steps=[
                ("Simple Imputer", SimpleImputer(strategy='mean')),
                ("Standard Scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline(steps=[
                ("Imputer", SimpleImputer(strategy="most_frequent")),
                ("OneHotEncoder", OneHotEncoder())
            ])

            transform_object = ColumnTransformer(transformers=[
                ("Numerical Transformers", num_pipeline, numerical_columns),
                ("Categorical Transformers", cat_pipeline, categorical_columns)
            ])

            return transform_object
        except Exception as e:
            raise CustomException(e, sys)

    def start_transformation(self, train_path, test_path):
        try:
            train_dataset = pd.read_csv(train_path)
            test_dataset = pd.read_csv(test_path)
            logging.info("Train and Test Dataset Read Complete")

           #Removing White Spaces
            train_dataset.columns = train_dataset.columns.str.strip()
            test_dataset.columns = test_dataset.columns.str.strip()

            # Print columns for debugging
            logging.info(f"Train Dataset columns after stripping: {train_dataset.columns.tolist()}")
            logging.info(f"Test Dataset columns after stripping: {test_dataset.columns.tolist()}")

            preprocessor_object = self.TransformerFunction()
            target_col = "Calories"

            input_cols_train = train_dataset.drop(columns=[target_col], axis=1)
            target_col_train = train_dataset[target_col]

            input_cols_test = test_dataset.drop(columns=[target_col], axis=1)
            target_col_test = test_dataset[target_col]

            logging.info("Applying preprocessing to Train and Test Dataframes")

            input_dataset_train_arr = preprocessor_object.fit_transform(input_cols_train)
            input_dataset_test_arr = preprocessor_object.transform(input_cols_test)

            train_arr = np.c_[input_dataset_train_arr, np.array(target_col_train)]
            test_arr = np.c_[input_dataset_test_arr, np.array(target_col_test)]
            
            logging.info("Saved preprocessing object.")

            save_object(
                file_path=self.obj_path.preprocess_obj_path,
                obj=preprocessor_object
            )

            return (
                train_arr,
                test_arr,
                self.obj_path.preprocess_obj_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
