import os
import sys
from xgboost import XGBRegressor

from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import r2_score
from src.utils import save_object

from sklearn.model_selection import GridSearchCV
class TrainerConfig():
    model_obj_path=os.path.join("Artifacts","model.pkl")

class Trainer():
    def __init__(self):
        self.trainer_path=TrainerConfig()
    #Since we already know XGB works the best on our Dataset, we will create the component based on it
    def start_Training(self,train_arr,test_arr):
        try:
            logging.info("Split Train and Test input Data")
            X_train,X_test,y_train,y_test=(
            train_arr[:,:-1],
            test_arr[:,:-1],
            train_arr[:,-1],
            test_arr[:,-1]
            )
            xgb=XGBRegressor()
            param={
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                   }
                    
            gs = GridSearchCV(xgb,param,cv=3)
            gs.fit(X_train,y_train)

            xgb.set_params(**gs.best_params_)
            xgb.fit(X_train,y_train)
            predicted=xgb.predict(X_test)
            r2=r2_score(y_test,predicted)
            save_object(
                file_path=self.trainer_path.model_obj_path,
                obj=xgb
            )
            return r2
        except Exception as e: 
            raise CustomException(e,sys)