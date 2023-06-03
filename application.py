from flask import Flask,render_template,request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.Pipeline import predict_pipeline,CustomData
application = Flask(__name__)
app = application
@app.route('/')
def index():
    render_template('index.html')
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_data = data.get_data_as_data_frame()
        print(pred_data)
        PredictPipeline = predict_pipeline()
        results = PredictPipeline.predict(pred_data)
        return render_template('home.html',results[0])
    


if __name__=="__main__":
    app.run(host="0.0.0.0")        

