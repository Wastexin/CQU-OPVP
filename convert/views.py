# -*- coding: utf-8 -*-
# coding: utf-8
#
# 忽略版本警告
import warnings

warnings.filterwarnings('ignore')
import pandas as pd
from cdkfingerprint import *
from rdkitfingerprint import *
from flask import Response
from flask_csv import send_csv
from flask import send_file, send_from_directory


def FingerprintType(fingerprintindex):
    if fingerprintindex == 0:
        # print('RDKIT-DaylightFingerprint')
        return GetRdkitDaylightFingerprint
    elif fingerprintindex == 1:
        # print('RDKIT-TopologicalTorsionFingerprint')
        return GetRdkitTopologicalTorsionFingerprint
    elif fingerprintindex == 2:
        return GetRdkitAtomPairFingerprint
    elif fingerprintindex == 3:
        return GetRdkitEstateFingerprint
    elif fingerprintindex == 4:
        return GetRdkitRDKFingerprint
    elif fingerprintindex == 5:
        return GetRdkitMACCSFingerprint
    elif fingerprintindex == 6:
        return GetRdkitMorganFingerprint
    elif fingerprintindex == 7:
        return GetCDKMACCSFingerPrint
    elif fingerprintindex == 8:
        return GetCDKPubchemFingerprint
    elif fingerprintindex == 9:
        return GetCDKExtendedFingerprint
    elif fingerprintindex == 10:
        return GetCDKHybridizationFingerprint
    else:
        pass

def SingleSmilesConvert(func, smiles, savename):
    all = []
    fingerprint = func(smiles).tolist()
    #print(fingerprint)
    add = []
    add.append(smiles)
    add.append(fingerprint)
    all.append(add)
    # 格式转换
    df = pd.DataFrame(all)
    # 保存为csv文件
    df.to_csv(savename, index=False, sep=',')




def FileSmilesConvert(func, namecol, PCEcol, smilescol, filename, savename):
    data = pd.read_csv(filename, header=None, encoding='gbk')
    #print(data)
    all = []
    # 对读取的数据进行遍历，当前数据的第三列是SMILES，第八列是PCE， 第二列是材料名称
    for index, row in data.iterrows():
        try:
            # 对每行的第二列进行读取，获取SMILES
            Smiles = row[smilescol]
            #print(Smiles)
            # 使用SMILES_to_fingerprint 里的函数进行转换，并转换为列表
            fingerprint = func(Smiles).tolist()
            #print(fingerprint)
            # 获取PCE
            PCE = row[PCEcol]
            # 获取名称
            name = row[namecol]
            # 用于保存每次遍历的结果，得到一行的数据，顺序为: name smiles PCE fingerprint
            add = []
            add.append(name)
            add.append(Smiles)
            add.append(PCE)
            add.append(fingerprint)
            # 加入到全部结果中
            all.append(add)
            # 遍历结束后便得到以每一个元素为数据列表的列表（得到一个元素为列表的列表）
        except Exception as e:
            print(e)

    # 格式转换
    df = pd.DataFrame(all)
    # 保存为csv文件

    df.to_csv(savename, index=False, sep=',')





if __name__ == '__main__':
    FileSmilesConvert(FingerprintType(1), filename='../uploads/fingerprint.csv',savename='../csv/fingerprint.csv',namecol=1, PCEcol=2, smilescol=3)
    pass
    #SingleSmilesConvert(GetRdkitMorganFingerprint, 'C(C=CC1)=C(C=1C(=O)O)O')