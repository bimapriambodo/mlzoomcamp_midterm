# Midterm_mlzoomcamp
## Lending Club Dataset Kaggle

> ### 1. Bussiness Understanding
Lending club is a p2p lending company, nowadays everyone can invest. From the company's point of view, borrowers with high credit scores (more trustworthy and less risky) thus earn lower interest rates on their loans, while borrowers with lower credit scores (less trustworthy and riskier) earn lower interest rates. higher. From the perspective of investors or lenders, loans with higher interest rates are more attractive because they provide a higher rate of return on investment (ROI) but on the other hand carry the risk of not being returned at all (default). The investment principle is high risk high return. However, here we will try to minimize the risk for large-risk loans. 

```The goal is to create an artificial intelligence model to predict which loans are likely to good out of all high-risk loans. It will be an attractive added value if you can select a loan with high interest but low probability of default.```


> ### 2. Define Target Definitions (Label)
Based on white paper by Dr. Ronen Meiri from DMWay Analytics **It makes sense in this case to define bad loans as “Charged Off” and the population as all the other loans that are (“fully paid”).?**

```“Does not meet the credit policy. Status: Charged Off” and “Does not meet the credit policy. Status: Fully Paid.” It is not clear why loans are given to users that “Does not meet the credit policy” and there is not much documentation on these categories. Now we need to define what is considered a “bad loan.” For example, is a loan payment that is 16 days overdue considered a bad loan? Such a loan does possess more risk than a fully payed loan, but it is still in the process of collection.```

The paper you can check on folder ```References.```

> ### 3. Tutorial Run Notebook and Train.py
1. First you must create virtual enviroment, for example if you use anaconda env, you can use these sintax: ```conda create -n yourenvname python=x.x anaconda``` then ```activate yourenvname```
2. After create the virtual env, you have to install all **requirements.txt** use this sintax: ```pip install -r requirements.txt```
3. Open the Jupyter Notebook, and select notebook.ipynb. This notebook containing Exporatory Data Analysis (EDA) till modelling.
4. Train.py used for direct modeling and generating pickle files, i recommend you read the notebook first.
