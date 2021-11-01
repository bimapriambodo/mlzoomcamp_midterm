from pydantic import BaseModel, validator
import json
import numpy as np

# 2. Class which describes Bank Notes measurements
class lendingclub(BaseModel):
    total_rec_int: float 
    total_rec_late_fee : float 
    term: str 
    installment: float
    funded_amnt: float
    loan_amnt: float
    dti: float
    funded_amnt_inv: float
    annual_inc: float
    grade: str
    home_ownership: str
    mo_sin_old_rev_tl_op: float
    tot_hi_cred_lim: float
    acc_open_past_24mths: float
    num_rev_tl_bal_gt_0: float

    @validator("term")
    def term_must_be_string(cls,v):
        if v.isdigit():
            raise ValueError("term Variable must be String")
        return v
    @validator("grade")
    def grade_must_be_string(cls,v):
        if v.isdigit():
            raise ValueError("grade Variable must be String")
        return v
    @validator("home_ownership")
    def home_ownership_must_be_string(cls,v):
        if v.isdigit():
            raise ValueError("home_ownership Variable must be String")
        return v