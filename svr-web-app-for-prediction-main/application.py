import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

## import svr model
svr=pickle.load(open('C:/Users/anton/OneDrive/Documentos/Curso_ML/5_udemy/2_SVM/end_to_end_implementation/model/svr.pkl','rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        Saturday=float(request.form.get('Saturday'))
        Sunday = float(request.form.get('Sunday'))
        Thursday = float(request.form.get('Thursday'))
        Friday = float(request.form.get ('Friday'))
        Tip = float(request.form.get('Tip'))
        Sex = float(request. form.get ('Sex'))
        Smoker = float(request.form.get('Smoker'))
        Time = float(request.form.get('Time'))
        Size = float(request.form.get ('Size'))
        result=svr.predict([[Saturday,Sunday,Thursday,Friday,Tip,Sex,Smoker,Time,Size]])
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')



if __name__=="__main__":
    app.run(host="0.0.0.0")
