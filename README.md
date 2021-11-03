# Midterm_mlzoomcamp
## Lending Club Dataset Kaggle
Dataset can be downloaded at Kaggle https://www.kaggle.com/wordsforthewise/lending-club

> ### 1. Bussiness Understanding
Lending club is a p2p lending company, nowadays everyone can invest. From the company's point of view, borrowers with high credit scores (more trustworthy and less risky) thus earn lower interest rates on their loans, while borrowers with lower credit scores (less trustworthy and riskier) earn lower interest rates. higher. From the perspective of investors or lenders, loans with higher interest rates are more attractive because they provide a higher rate of return on investment (ROI) but on the other hand carry the risk of not being returned at all (default). The investment principle is high risk high return. However, here we will try to minimize the risk for large-risk loans. 

```The goal is to create an artificial intelligence model to predict which loans are likely to good out of all high-risk loans. It will be an attractive added value if you can select a loan with high interest but low probability of default.```


> ### 2. Define Target Definitions (Label)
Based on white paper by Dr. Ronen Meiri from DMWay Analytics **It makes sense in this case to define bad loans as “Charged Off” and the population as all the other loans that are (“fully paid”).**

```“Does not meet the credit policy. Status: Charged Off” and “Does not meet the credit policy. Status: Fully Paid.” It is not clear why loans are given to users that “Does not meet the credit policy” and there is not much documentation on these categories. Now we need to define what is considered a “bad loan.” For example, is a loan payment that is 16 days overdue considered a bad loan? Such a loan does possess more risk than a fully payed loan, but it is still in the process of collection.```

The paper you can check on folder ```References.```

> ### 3. Tutorial Run Notebook and Train.py
1. First you must create virtual enviroment, for example if you use anaconda env, you can use these sintax: 
```python
conda create -n yourenvname python=x.x anaconda
``` 
then 
```python
activate yourenvname
```
2. After create the virtual env, you have to install all **requirements.txt** use this sintax: ```pip install -r requirements.txt```
3. Open the Jupyter Notebook, and select **notebook.ipynb.** This notebook containing Exporatory Data Analysis (EDA) till modelling.
4. Train.py used for direct modeling and generating pickle files, i recommend you read the notebook first.

> ### 3. Tutorial Run API Webservice
1. First you have to install Docker, you can donwloaded at https://www.docker.com/
2. Because this api deploy to Heroku, you need register first to https://id.heroku.com/login
3. Install Heroku Cli for windows (if you use windows)
4. Then open CMD, you need enter the to directory API
5. Then please follow this sintax one by one
```python
heroku login
```
after login, you need login to Heroku container
```python
heroku container:login
```
then you have to make app from Heroku
```python
heroku create YOUR_UNIQUE_NAME
```
after that push the container to the heroku using command
```python
heroku container:push web --app YOUR_UNIQUE_NAME
```
Finaly release the api web service using command
```python
heroku container:release web --app YOUR_UNIQUE_NAME
```
6. After deploy the container to heroku, you can test the api with Json format
https://[YOUR_UNIQUE_NAME].herokuapp.com/predict

In this case you can try my own webservice
https://lendingclub-zoom.herokuapp.com/predict

this example format:
```JSON
{"total_rec_int": 0.0,
  "total_rec_late_fee": 0.0,
  "term": "string",
  "installment": 0.0,
  "funded_amnt": 0.0,
  "loan_amnt": 0.0,
  "dti": 0.0,
  "funded_amnt_inv": 0.0,
  "annual_inc": 0.0,
  "grade": "string",
  "home_ownership": "string",
  "mo_sin_old_rev_tl_op": 0.0,
  "tot_hi_cred_lim": 0.0,
  "acc_open_past_24mths": 0.0,
  "num_rev_tl_bal_gt_0": 0.0}
  ```
___

| VARIABLES        | DATA TYPE           |
| ------------- |:-------------:| 
| total_rec_ints      | FLOAT | 
| total_rec_late_fee      | FLOAT      |
| term | STRING      | 
| installment | FLOAT |
| funded_amnt | FLOAT |
| loan_amnt | FLOAT |
| dti | FLOAT |
| funded_amnt_inv | FLOAT |
| annual_inc | FLOAT |
| grade | STRING |
| home_ownership | STRING |
| mo_sin_old_rev_tl_op | FLOAT |
| tot_hi_cred_lim | FLOAT |
| acc_open_past_24mths | FLOAT |
| num_rev_tl_bal_gt_0 | FLOAT |

___
