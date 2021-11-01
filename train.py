import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import auc,confusion_matrix, cohen_kappa_score, accuracy_score, roc_auc_score, roc_curve, precision_recall_curve, f1_score, recall_score, precision_score
from catboost import Pool, CatBoostClassifier
import pickle

print("select and filter data")
df = pd.read_csv(r"accepted_2007_to_2018Q4.csv")
df_ = df[df["grade"].isin(['E','F','G'])]
df_['target'] = df_['loan_status'].apply(lambda x: 1 if x=='Fully Paid' else 0 if x == 'Charged Off' else 2)
df_ = df_[~(df_["target"]==2)]
# print(df_.shape)

print('handling missing values')
df_['earliest_cr_line'] = pd.to_datetime(df_['earliest_cr_line'], infer_datetime_format=True)
df_['issue_d'] = pd.to_datetime(df_['issue_d'], infer_datetime_format=True)
fill_na = ['emp_title']
fill_max = ['bc_open_to_buy', 'mo_sin_old_il_acct', 'mths_since_rcnt_il', 'mths_since_recent_bc', 'mths_since_recent_inq', 'pct_tl_nvr_dlq']
fill_min = df_.loc[:,~(df_.columns.isin(fill_na+fill_max))].columns
df_[fill_na] = df_[fill_na].fillna('not_avalaible')
df_[fill_max] = df_[fill_max].fillna(df_[fill_max].max())
df_[fill_min] = df_[fill_min].fillna(-9999)
# print(df_.shape)

print('SPLIT DATA DEV AND DATA OOT')
df_dev = df_[df_['issue_d']<='2018-09-30']
df_oot = df_[df_['issue_d']>='2018-10-01'] # Q4 2018
df_oot['data_types'] = 'oot'
# print(df_dev.shape)
# print(df_oot.shape)

X = df_dev.loc[:, df_dev.columns != 'target']
y = df_dev[['target']]

# print(X.shape)
# print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
data_train = pd.concat([X_train,y_train], axis=1)
data_train['data_types'] ='train'
data_test = pd.concat([X_test,y_test], axis=1)
data_test['data_types'] ='test'
data_dev = pd.concat([data_train,data_test])

df_ = pd.concat([data_dev,df_oot])
# print(df_.shape)

cat_feat_ind2 = ['term', 'grade', 'home_ownership']
selected_fix = ['total_rec_int', 'total_rec_late_fee', 'term', 'installment', 'funded_amnt', 'loan_amnt', 'dti', 'funded_amnt_inv', 'annual_inc', 'grade',
                'home_ownership', 'mo_sin_old_rev_tl_op', 'tot_hi_cred_lim', 'acc_open_past_24mths', 'num_rev_tl_bal_gt_0']

X_train2 = df_[df_['data_types']=='train'][selected_fix]
y_train2 = df_[df_['data_types']=='train']['target']
X_test2 = df_[df_['data_types']=='test'][selected_fix]
y_test2 = df_[df_['data_types']=='test']['target']
X_oot2 = df_[df_['data_types']=='oot'][selected_fix]
y_oot2 = df_[df_['data_types']=='oot']['target']

print("MODEL BUILD")
pool_train2 = Pool(X_train2, y_train2, cat_features=cat_feat_ind2)
pool_test2 = Pool(X_test2, y_test2, cat_features=cat_feat_ind2)
pool_val2 = Pool(X_oot2, y_oot2, cat_features=cat_feat_ind2)

n2 = y_train2.value_counts()

tunned_model = CatBoostClassifier(learning_rate=0.03,
                                  iterations=1000,
                                  early_stopping_rounds=100,
                                  class_weights=[1, n2[0] / n2[1]],
                                  verbose=False,
                                  random_state=0,
                                  l2_leaf_reg=3,
                                  bagging_temperature=1,
                                  random_strength=1,
                                  one_hot_max_size=2,
                                  leaf_estimation_method='Newton')

tunned_model.fit(pool_train2, eval_set=pool_test2)

best_model = CatBoostClassifier(
    random_state=0,
    iterations=int(tunned_model.tree_count_ * 1.2),)

best_model.fit(
    pool_train2,
    verbose=100)

y_pred_oot = best_model.predict(pool_val2)
acc_test = accuracy_score(y_oot2, y_pred_oot)
prec_test = precision_score(y_oot2, y_pred_oot)
rec_test = recall_score(y_oot2, y_pred_oot)
print(f'''Accuracy (OOT): {acc_test:.3f}
Precision (OOT): {prec_test:.3f}
Recall (OOT): {rec_test:.3f}''')
print("AUC of ROC OOT:" + str(roc_auc_score(y_oot2,y_pred_oot)))

print("MODEL SAVING")
Pkl_Filename = "catboost_v1.pkl"  
with open(Pkl_Filename, 'wb') as file:  
    pickle.dump(best_model, file)

