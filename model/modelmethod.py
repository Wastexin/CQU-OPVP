# -*- coding: utf-8 -*-
# coding: utf-8
# @Author  : WeiXin
# 忽略版本警告
import warnings

warnings.filterwarnings('ignore')
import joblib
from rdkitfingerprint import *
#from smilesmethod import *
from cdkfingerprint import *
import pickle

def SelectAlgorithm(algorithmtype):
    if algorithmtype == 1:
        al = joblib.load('G:/Graduation Design/ML/Software/Gui/joblib/gbdt.joblib')
    elif algorithmtype ==2:
        al = joblib.load('G:/Graduation Design/ML/Software/Gui/joblib/RandomForest_Regression_Morgan.pkl')
    elif algorithmtype ==3:
        al = joblib.load('G:/Graduation Design/ML/Software/Gui/joblib/SVM_Regression_Hybridization.pkl')
    return al

def ClassifierPredit(smiles, al):
    fingerprint = GetRdkitDaylightFingerprint(smiles).reshape(1, 1024)
    print(fingerprint.shape)
    model = SelectAlgorithm(algorithmtype=al)
    model.predict(fingerprint)
    prob = model.predict_proba(fingerprint)
    target = model.predict(fingerprint)
    return prob, target

def RegressionPredit(smiles, al):
    if al == 3:
        fingerprint = GetCDKHybridizationFingerprint(smiles).reshape(1, 1024)
    elif al == 2:
        fingerprint = GetRdkitMorganFingerprint(smiles).reshape(1, 2048)
    elif al == 1:
        fingerprint = GetRdkitDaylightFingerprint(smiles).reshape(1, 1024)
    #fingerprint = GetRdkitMorganFingerprint(smiles).reshape(1, 2048)
    print(fingerprint.shape)
    model = SelectAlgorithm(algorithmtype=al)
    PCE = model.predict(fingerprint)
    #print(str(PCE[0]))
    return str(PCE[0])
    #prob = model.predict_proba(fingerprint)
    #target = model.predict(fingerprint)
    #return prob, target


if __name__ == '__main__':
    smiles = 'O=C1C(C2=C(O)C=C(N(C(C)CC)CCC)C=C2O)=C([O-])/C1=C(C(O)=C/3)\C(O)=CC3=[N+](CCC)\C(C)CC'
    startJVM(getDefaultJVMPath(), "-ea")
    print(RegressionPredit(smiles, 2))
    #ClassifierPredit(smiles, 1)
    #prob = Regrepredit(smiles, 1)
    #print(type(str(prob[0][0])))
    #print(target)
    #predit(smiles,1)