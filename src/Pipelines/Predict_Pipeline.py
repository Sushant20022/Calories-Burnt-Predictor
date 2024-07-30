from src.exception import CustomException
from src.utils import load_object
import sys
import pandas as pd
import os

class Prediction:
    def __init__(self):
        pass
    def predict(self,colmns):
        try:
            model_path=os.path.join("Artifacts","model.pkl")
            preprocessor_path=os.path.join("Artifacts","preprocessor.pkl")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data=preprocessor.transform(colmns)
            result=model.predict(data)
            return result
        except Exception as e:
            raise CustomException(e,sys) 

class FormData:
    def __init__(self,
    Gender:str,
    Age: int,
    Height:float,
    Weight:float,
    Duration:float,
    Heart_Rate:float,
    Body_Temp:float ):
        
        self.Gender=Gender
        self.Age=Age
        self.Height=Height
        self.Weight=Weight    
        self.Duration =Duration
        self.Heart_Rate=Heart_Rate         
        self.Body_Temp=Body_Temp         
   
   
    def convert_to_Dataframe(self):
        try:
             custom_dict={
             "Gender":[self.Gender],
             "Age":[self.Age],
             "Height":[self.Height],
             "Weight":[self.Weight],
             "Duration":[self.Duration],
             "Heart_Rate":[self.Heart_Rate],
             "Body_Temp":[self.Body_Temp],
             }
             print(custom_dict)
             return pd.DataFrame(custom_dict)
        
        except Exception as e:
            raise CustomException(e,sys) 
                
