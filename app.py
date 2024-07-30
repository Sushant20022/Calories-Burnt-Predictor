from flask import Flask,render_template,request
from src.Pipelines.Predict_Pipeline import Prediction,FormData
import numpy as np
import pandas as pd


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('main.html')
    else:
        data=FormData(
        Gender=request.form['gender'],
        Age=int(request.form['age']),
        Height=float(request.form['height']),
        Weight=float(request.form['weight']),
        Duration=float(request.form['duration']),
        Heart_Rate=float(request.form['heartRate']),
        Body_Temp=float(request.form['bodyTemprature'])
         )
        df=data.convert_to_Dataframe()
        print(df)

        predict_pipeline=Prediction()
        result=predict_pipeline.predict(df)
        return render_template('main.html',calories=result[0])
if __name__=="__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        print("Cant run")