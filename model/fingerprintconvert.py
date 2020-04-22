# -*- coding: utf-8 -*-
# coding: utf-8
# @Author  : WeiXin

from rdkitfingerprint import *
import numpy as np
import pandas as pd
from cdkfingerprint import *


# pd.set_option('display.max_columns',2048)
# pd.set_option('display.width', 2048)
# pd.set_option('display.max_colwidth', 2048)

#globals()


def SingleSmilesConvert(func, smiles, savename='fingerprint.csv'):
    all = []
    fingerprint = func(smiles).tolist()
    print(fingerprint)
    add = []
    add.append(smiles)
    add.append(fingerprint)
    all.append(add)
    # 格式转换
    df = pd.DataFrame(all)
    # 保存为csv文件
    df.to_csv(savename, index=False, sep=',')

def FileSmilesConvert(func, filename, namecol, PCEcol, smilescol):
    data = pd.read_csv(filename, header=None, encoding='gbk')
    all = []
    # 对读取的数据进行遍历，当前数据的第三列是SMILES，第八列是PCE， 第二列是材料名称
    for index, row in data.iterrows():
        try:
            # 对每行的第二列进行读取，获取SMILES
            Smiles = row[smilescol]
            # 使用SMILES_to_fingerprint 里的函数进行转换，并转换为列表
            fingerprint = func(Smiles).tolist()
            print(fingerprint)
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
    savename = filename + 'fingerprint.csv'
    df.to_csv(savename, index=False, sep=',')

# def FingerPrint_Convert(func, filename=None, namecol=None, PCEcol=None, smilescol=None, smiles=0, savename='fingerprint.csv'):
#
#     # 用于保存结果
#     all = []
#     # 单个smiles输入时
#     if smiles != 0:
#         try:
#             #print(func)
#             #print('ftc')
#             fingerprint = func(smiles).tolist()
#             #print(len(fingerprint))
#             print(fingerprint)
#             add = []
#             add.append(smiles)
#             add.append(fingerprint)
#             all.append(add)
#             # 格式转换
#             df = pd.DataFrame(all)
#             # 保存为csv文件
#             df.to_csv(savename,index=False,sep=',')
#         except Exception as e:
#             print(e)
#
#
#
#     else:
#
#         # 读取数据
#         data = pd.read_csv(filename, header=None, encoding='gbk')
#
#         # 对读取的数据进行遍历，当前数据的第三列是SMILES，第八列是PCE， 第二列是材料名称
#         for index, row in data.iterrows():
#             try:
#                 # 对每行的第二列进行读取，获取SMILES
#                 Smiles = row[smilescol]
#                 # 使用SMILES_to_fingerprint 里的函数进行转换，并转换为列表
#                 fingerprint = func(Smiles).tolist()
#                 # 获取PCE
#                 PCE = row[PCEcol]
#                 # 获取名称
#                 name = row[namecol]
#                 # 用于保存每次遍历的结果，得到一行的数据，顺序为: name smiles PCE fingerprint
#                 add = []
#                 add.append(name)
#                 add.append(Smiles)
#                 add.append(PCE)
#                 add.append(fingerprint)
#                 # 加入到全部结果中
#                 all.append(add)
#                 # 遍历结束后便得到以每一个元素为数据列表的列表（得到一个元素为列表的列表）
#             except Exception as e:
#                 print(e)
#
#         # 格式转换
#         df = pd.DataFrame(all)
#         # 保存为csv文件
#         df.to_csv(savename,index=False,sep=',')
#
#
#     #print(type(df))


if __name__ == '__main__':
    try:
        smiles = 'O=C1C(C2=C(O)C=C(N(C(C)CC)CCC)C=C2O)=C([O-])/C1=C(C(O)=C/3)\C(O)=CC3=[N+](CCC)\C(C)CC'
        startJVM(getDefaultJVMPath(), "-ea")
        SingleSmilesConvert(func=GetCDKPubchemFingerprint, smiles=smiles)
        shutdownJVM()
    except Exception as e:
        print(e)
