# 1. Library imports
import uvicorn
from fastapi import FastAPI
from lendingclub import LendingClub
import numpy as np
import pickle
import pandas as pd
from catboost import Pool, CatBoostClassifier

app = FastAPI(
    title="MIDTERM PROJECT ZOOMCAMP - LENDING CLUB PROJECT",
    version="1.0.0"
)

pickle_in = open("catboost_v1.pkl","rb")
model=pickle.load(pickle_in)
x = None

def predict(data,model):
    df = pd.DataFrame.from_dict(data,orient='index').T
    # print(df)
    cat_feat_ind2=['term', 'grade', 'home_ownership']
    df = Pool(df, cat_features=cat_feat_ind2)
    # print(df)
    y_pred_train = model.predict_proba(df)[:,1]*100
    return y_pred_train[0]

@app.post('/predict')
def predict_loan(data:LendingClub):
    data = data.dict()
    # print(data)

    prediction = predict(data,model)
    # print(prediction)

    if(prediction>50):
        x='Good Loan'
    else:
        x='Bad Loan'
    result = dict()
    result.update(proba = prediction, pred = x)
    return result

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)