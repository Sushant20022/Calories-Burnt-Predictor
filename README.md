# Calories-Burnt-Predictor
Repository storing the Packages for a Machine Learning Predictor to Predict the Calories Burnt by a Person  
 VideoLink for defining the DataSet : https://youtu.be/21nsGTBFE4M?si=FxFx76GoOuUPW8AU
 Kaggle Link to Download Dataset : https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos/data 

# Approach for the project
## Data Ingestion :

In Data Ingestion phase the input data is first read as csv file.
Afterwards this data is splitted into training and testing and saved as csv files named Train.csv and Test.csv.
## Data Transformation :

In this phase a ColumnTransformer Pipeline is created which Preprocesses the Respective Columns in the Dataset.
for Numeric Variables first SimpleImputer is applied with strategy mean, then Standard Scaling is performed on all numerical columns of the data.
for Categorical Variables SimpleImputer is applied with most frequent strategy, then one hot encoding performed ,since there is only 1 categorical column(gender). 
This preprocessor is saved as pickle file in the repository.
## Model Training :

In this step the base model is tested .The best model found was XGBregressor in the Model Training File against a list of Various models.Hence the Model is created using XGBRegressor.
After this hyperparameter tuning is performed on XGboost.
This model is saved as pickle file.
## Prediction Pipeline :

This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.
## Flask App creation :

Flask app is created with User Interface to predict the Calories Burnt, inside a Web Application.
Exploratory Data Analysis Notebook
Link : [View Link](https://github.com/Sushant20022/Calories-Burnt-Predictor/blob/main/projectfolder_Calories/EDA.ipynb)

Model Training Approach Notebook
Link : [View Link](https://github.com/Sushant20022/Calories-Burnt-Predictor/blob/main/projectfolder_Calories/MODEL_TRAINING.ipynb)


# ScreenShot of UI 

<p><img align="left" src="https://github.com/Sushant20022/Calories-Burnt-Predictor/blob/main/templates/SampleUI.png" alt="sushant20022" /></p>

# Note : 
This project is yet to be Deployed on Any Major Cloud Infrastructure. It works only on Local Machines (LOCALHOST:5000).

:))
