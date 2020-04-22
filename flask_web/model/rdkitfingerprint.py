# -*- coding: utf-8 -*-
# coding: utf-8
# @Author  : WeiXin

from rdkit import DataStructs
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import MACCSkeys
from rdkit.Chem import DataStructs
from rdkit.Chem.AtomPairs import Pairs
import numpy as np
import fingerprint


'''
    #####################
    # 本模块基于中南大学药学院计算生物学与药物设计小组的ChemDes项目
    #####################
'''


''' 
    ######################
    # MACCSFingerprint 166bits
    ######################
'''
def GetRdkitMACCSFingerprint(smiles):
    '''
        return a MACCS fingerprint vector （166bits）
    '''
    # 根据smiles转换成RDkit里的Mol Object
    mol = Chem.MolFromSmiles(smiles)
    # 由项目的模块获取指纹，返回的是{位置：1}的键值对（只有为1的键值对，没有0的）
    MACCS_fingerprint = fingerprint.CalculateMACCSFingerprint(mol)[1]
    # 获取指纹位数
    length = fingerprint.CalculateMACCSFingerprint(mol)[0]
    # 重构分子指纹，在所有位置添加0，1
    for i in range(length):
        if MACCS_fingerprint.get(i) == None:
            MACCS_fingerprint.setdefault(i, 0)
        else:
            MACCS_fingerprint.setdefault(i, 1)

    # 从0重新开始排序
    vec_dict = dict(sorted(MACCS_fingerprint.items(), key=lambda d: d[0]))
    # 格式转换
    vec_list = list(vec_dict.values())
    vec_nparray = np.array(vec_list)
    # 输出np数组
    return vec_nparray


''' 
    ######################
    # MorganFingerprint 1024bits default
    ######################
'''
def GetRdkitMorganFingerprint(Smiles, nBits=2048):
    '''
        return a np.array which contain 2048bits(default) vector
    '''
    # 根据smiles转换成RDkit里的Mol Object
    mol = Chem.MolFromSmiles(Smiles)
    # 根据RDkit里的Morgan指纹函数进行转换
    fingerprint_morgan = AllChem.GetMorganFingerprint(mol, 2)
    # 转换为Morgan指纹向量
    fingerprint_morgan_hashed = AllChem.GetMorganFingerprintAsBitVect(mol,2, nBits=nBits)
    # 格式转换
    fingerprint_list = list(fingerprint_morgan_hashed.ToBitString())
    new_list = list(map(int, fingerprint_list))
    # 输出数组
    return np.array(new_list)


''' 
    ######################
    # TopologicalTorsionFingerprint 1024bits default
    ######################
'''
def GetRdkitTopologicalTorsionFingerprint(Smiles, nBits=1024):
    '''
        return a np.array which contain 2048bits(default) vector
    '''
    # 转换过程同Morgan指纹
    mol = Chem.MolFromSmiles(Smiles)
    fingerprint_TopologicalTorsion = AllChem.GetHashedTopologicalTorsionFingerprintAsBitVect(mol, nBits=nBits)
    fingerprint_list = list(fingerprint_TopologicalTorsion.ToBitString())
    new_list = list(map(int, fingerprint_list))
    return np.array(new_list)


''' 
    ######################
    # AtomPairFingerprintFingerprint  1024bits default
    ######################
'''
def GetRdkitAtomPairFingerprint(Smiles, nBits=1024):
    '''
        return a np.array which contain 2048bits(default) vector
    '''
    #转换过程同Morgan指纹
    mol = Chem.MolFromSmiles(Smiles)
    fingerprint_AtomPairFingerprint = AllChem.GetHashedAtomPairFingerprintAsBitVect(mol, nBits=nBits)
    fingerprint_list = list(fingerprint_AtomPairFingerprint.ToBitString())
    new_list = list(map(int, fingerprint_list))
    return np.array(new_list)

''' 
    ######################
    # DaylightFingerprint 1024bits
    ######################
'''
# def GetRdkitDaylightFingerprint(smiles):
#     '''
#         return a daylight fingerprint vector （1024bits）
#     '''
#     # 转换过程同MACCS指纹
#     mol = Chem.MolFromSmiles(smiles)
#     Dayligth_fingerprint = fingerprint.CalculateDaylightFingerprint(mol)[1]
#     #print(fingerprint.CalculateDaylightFingerprint(mol))
#     #print(fingerprint.CalculateDaylightFingerprint(mol)[0])
#     print(Dayligth_fingerprint)
#     #print(Dayligth_fingerprint.keys())
#     length = fingerprint.CalculateDaylightFingerprint(mol)[0]
#     print(length)
#     for i in range(length):
#         if Dayligth_fingerprint.get(i) == None:
#             Dayligth_fingerprint.setdefault(i, 0)
#         else:
#             Dayligth_fingerprint.setdefault(i, 1)
#     vec_dict = dict(sorted(Dayligth_fingerprint.items(), key=lambda d: d[0]))
#     vec_list = list(vec_dict.values())
#     vec_nparray = np.array(vec_list)
#     return vec_nparray

''' 
    ######################
    # E-stateFingerprint  79bits
    ######################
'''
def GetRdkitEstateFingerprint(smiles):
    '''
        return a E-state fingerprint vector （79bits）
    '''
    # 转换过程同MACCS指纹
    mol = Chem.MolFromSmiles(smiles)
    Estate_fingerprint = fingerprint.CalculateEstateFingerprint(mol)[1]
    #print(Estate_fingerprint.keys())
    length = fingerprint.CalculateEstateFingerprint(mol)[0]
    for i in range(length):
        if Estate_fingerprint.get(i) == None:
            Estate_fingerprint.setdefault(i, 0)
        else:
            Estate_fingerprint.setdefault(i, 1)

    vec_dict = dict(sorted(Estate_fingerprint.items(), key=lambda d: d[0]))
    vec_list = list(vec_dict.values())
    vec_nparray = np.array(vec_list)
    return vec_nparray

''' 
    ######################
    # RDKFingerprint 2048bits default
    ######################
'''
def GetRdkitRDKFingerprint(smiles):
    '''
        return a RDK fingerprint vector (it seems like daylight fingerprint)
    '''
    # 转换过程同MACCS指纹
    mol = Chem.MolFromSmiles(smiles)
    fps = Chem.RDKFingerprint(mol)
    a = []
    for i in fps:
        a.append(i)
    vec_nparray = np.array(a)
    return vec_nparray

''' 
    ######################
    # RDKFingerprint 1024bits
    ######################
'''

def GetRdkitDaylightFingerprint(smiles):
    mol = Chem.MolFromSmiles(smiles)
    fps = Chem.RDKFingerprint(mol, fpSize=1024)
    a = []
    for i in fps:
        a.append(i)
    vec_nparray = np.array(a)
    return vec_nparray


if __name__=="__main__":
    #smiles = 'O=C(N1CCC(CCCCCCCC)CCCCCCCCCC)C2=C(C3=CC4=C(S3)C(CCCCCC)=C(C5=CC6=C(C7=CC=C(CCC(CCCC)CC)S7)C8=C(C=C([*])S8)C(C9=CC=C(CCC(CCCC)CC)S9)=C6S5)S4)SC(C%10=CC(SC([*])=C%11CCCCCC)=C%11S%10)=C2C1=O'
    smiles = 'O=C1C(C2=C(O)C=C(N(C(C)CC)CCC)C=C2O)=C([O-])/C1=C(C(O)=C/3)\C(O)=CC3=[N+](CCC)\C(C)CC'
    # print(GetRdkitAtomPairFingerprint(smiles).tolist())
    # print(GetRdkitDaylightFingerprint(smiles).tolist())
    # print(GetRdkitEstateFingerprint(smiles).tolist())
    # print(GetRdkitMACCSFingerprint(smiles).tolist())
    # print(GetRdkitMorganFingerprint(smiles).tolist())
    # print(GetRdkitDaylightFingerprint(smiles).tolist())
    # print(GetRdkitTopologicalTorsionFingerprint(smiles).tolist())
    print(GetRdkitDaylightFingerprint(smiles).shape)