# -*- coding: utf-8 -*-
# coding: utf-8
# @Author  : WeiXin
# 忽略版本警告
import warnings

warnings.filterwarnings('ignore')
from jpype import *
import jpype.imports
from jpype.types import *
import os.path
import numpy as np



import joblib
from rdkitfingerprint import *
from cdkfingerprint import *
import pickle


def SelectAlgorithm(algorithmtype):
    job = joblib.load('RandomForest_Regression_Morgan.pkl')
    if algorithmtype ==0:
        job = joblib.load('RandomForest_Regression_Morgan.pkl')
    elif algorithmtype ==1:
        job = joblib.load('SVM_Regression_Hybridization.pkl')
    elif algorithmtype == 2:
        job = joblib.load('gbdt.joblib')
    return job

def RegressionPredit(smiles, al):
    fingerprint = GetRdkitMorganFingerprint(smiles).reshape(1, 2048)
    if al == 1:
        fingerprint = GetCDKHybridizationFingerprint(smiles).reshape(1, 1024)
    elif al == 0:
        fingerprint = GetRdkitMorganFingerprint(smiles).reshape(1, 2048)
    elif al == 2:
        fingerprint = GetRdkitDaylightFingerprint(smiles).reshape(1, 1024)
    #fingerprint = GetRdkitMorganFingerprint(smiles).reshape(1, 2048)
    #print(fingerprint.shape)
    model = SelectAlgorithm(al)
    PCE = model.predict(fingerprint)
    #print(str(PCE[0]))
    return str(PCE[0])
    #prob = model.predict_proba(fingerprint)
    #target = model.predict(fingerprint)
    #return prob, target


if __name__ == '__main__':
    smiles = 'O=C1C(C2=C(O)C=C(N(C(C)CC)CCC)C=C2O)=C([O-])/C1=C(C(O)=C/3)\C(O)=CC3=[N+](CCC)\C(C)CC'
    startJVM(getDefaultJVMPath(), "-ea")
    print(RegressionPredit(smiles, 0))
    #ClassifierPredit(smiles, 1)
    #prob = Regrepredit(smiles, 1)
    #print(type(str(prob[0][0])))
    #print(target)
    #predit(smiles,1)