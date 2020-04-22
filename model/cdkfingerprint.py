# -*- coding: utf-8 -*-
# coding: utf-8
# @Author  : WeiXin

# 忽略版本警告
import warnings
warnings.filterwarnings('ignore')

# pyj4 jpype
from jpype import *
import jpype.imports
from jpype.types import *
import os.path
import numpy as np
jpype.addClassPath('cdk-2.3.jar')
#jpype.addClassPath('G:/Graduation Design/ML/flask/model/cdk-2.3.jar')

'''
    getFingerprint() 返回的是一个java.util.bitset
    必须转化成为python处理的类型    
'''
def JavaToPython(bitset):
    '''
        java.util.bitset 转化成python list
    '''
    bitset_str = bitset.toString()
    num_list = []
    # 进行字符串处理
    bitset_string = bitset_str.strip('{}').replace(' ','')
    bitset_list = bitset_string.split(',')
    for item in bitset_list:
        num_list.append(int(item))
    return num_list

''' 
    ######################
    # CDKMACCSFingerPrint 166bits
    ######################
'''
def GetCDKMACCSFingerPrint(smiles):
    jpype.addClassPath('cdk-2.3.jar')
    SmilesParser = jpype.JClass('org.openscience.cdk.smiles.SmilesParser')
    IChemObjectBuilder = jpype.JClass('org.openscience.cdk.interfaces.IChemObjectBuilder')
    DefaultChemObjectBuilder = jpype.JClass('org.openscience.cdk.DefaultChemObjectBuilder')
    IAtomContainer = jpype.JClass('org.openscience.cdk.interfaces.IAtomContainer')
    MACCSFingerprinter = jpype.JClass('org.openscience.cdk.fingerprint.MACCSFingerprinter')
    smilesParser = SmilesParser(DefaultChemObjectBuilder.getInstance())
    maccsfingerprinter = MACCSFingerprinter(DefaultChemObjectBuilder.getInstance())
    molecule = smilesParser.parseSmiles(smiles)
    fingerprint = maccsfingerprinter.getFingerprint(molecule)
    length = maccsfingerprinter.getSize()
    fingerprint_list = JavaToPython(fingerprint)
    fingerprint_dict = {}
    for i in range(length):
        if i in fingerprint_list:
            fingerprint_dict.setdefault(i, 1)
        else:
            fingerprint_dict.setdefault(i, 0)

    vec_list = list(fingerprint_dict.values())
    print(length)
    vec_nparray = np.array(vec_list)
    return vec_nparray

''' 
    ######################
    # CDKPubchemFingerprint 881bits
    ######################
'''
def GetCDKPubchemFingerprint(smiles):
    jpype.addClassPath('cdk-2.3.jar')
    SmilesParser = jpype.JClass('org.openscience.cdk.smiles.SmilesParser')
    IChemObjectBuilder = jpype.JClass('org.openscience.cdk.interfaces.IChemObjectBuilder')
    DefaultChemObjectBuilder = jpype.JClass('org.openscience.cdk.DefaultChemObjectBuilder')
    IAtomContainer = jpype.JClass('org.openscience.cdk.interfaces.IAtomContainer')
    MACCSFingerprinter = jpype.JClass('org.openscience.cdk.fingerprint.MACCSFingerprinter')
    smilesParser = SmilesParser(DefaultChemObjectBuilder.getInstance())
    PubchemFingerprinter = jpype.JClass('org.openscience.cdk.fingerprint.PubchemFingerprinter')
    molecule = smilesParser.parseSmiles(smiles)
    pubchemfingerprinter = PubchemFingerprinter(DefaultChemObjectBuilder.getInstance())
    fingerprint = pubchemfingerprinter.getFingerprint(molecule)
    length = pubchemfingerprinter.getSize()
    fingerprint_list = JavaToPython(fingerprint)
    fingerprint_dict = {}
    for i in range(length):
        if i in fingerprint_list:
            fingerprint_dict.setdefault(i, 1)
        else:
            fingerprint_dict.setdefault(i, 0)

    vec_list = list(fingerprint_dict.values())
    print(length)
    vec_nparray = np.array(vec_list)
    return vec_nparray

''' 
    ######################
    # CDKExtendedFingerprint 1024bits
    ######################
'''
def GetCDKExtendedFingerprint(smiles):
    jpype.addClassPath('cdk-2.3.jar')
    SmilesParser = jpype.JClass('org.openscience.cdk.smiles.SmilesParser')
    IChemObjectBuilder = jpype.JClass('org.openscience.cdk.interfaces.IChemObjectBuilder')
    DefaultChemObjectBuilder = jpype.JClass('org.openscience.cdk.DefaultChemObjectBuilder')
    IAtomContainer = jpype.JClass('org.openscience.cdk.interfaces.IAtomContainer')
    AtomContainer2 = jpype.JClass('org.openscience.cdk.AtomContainer$2')
    MACCSFingerprinter = jpype.JClass('org.openscience.cdk.fingerprint.MACCSFingerprinter')
    smilesParser = SmilesParser(DefaultChemObjectBuilder.getInstance())
    ExtendedFingerprinter = jpype.JClass('org.openscience.cdk.fingerprint.ExtendedFingerprinter')
    molecule = smilesParser.parseSmiles(smiles)
    extendedfingerprinter = ExtendedFingerprinter()
    fingerprint = extendedfingerprinter.getFingerprint(molecule)
    length = extendedfingerprinter.getSize()
    fingerprint_list = JavaToPython(fingerprint)
    fingerprint_dict = {}
    for i in range(length):
        if i in fingerprint_list:
            fingerprint_dict.setdefault(i, 1)
        else:
            fingerprint_dict.setdefault(i, 0)

    vec_list = list(fingerprint_dict.values())
    print(length)
    vec_nparray = np.array(vec_list)
    return vec_nparray

''' 
    ######################
    # CDKHybridizationFingerprint 1024bits
    ######################
'''
def GetCDKHybridizationFingerprint(smiles):
    jpype.addClassPath('cdk-2.3.jar')
    SmilesParser = jpype.JClass('org.openscience.cdk.smiles.SmilesParser')
    IChemObjectBuilder = jpype.JClass('org.openscience.cdk.interfaces.IChemObjectBuilder')
    DefaultChemObjectBuilder = jpype.JClass('org.openscience.cdk.DefaultChemObjectBuilder')
    IAtomContainer = jpype.JClass('org.openscience.cdk.interfaces.IAtomContainer')
    MACCSFingerprinter = jpype.JClass('org.openscience.cdk.fingerprint.MACCSFingerprinter')
    smilesParser = SmilesParser(DefaultChemObjectBuilder.getInstance())
    HybridizationFingerprinter = jpype.JClass('org.openscience.cdk.fingerprint.HybridizationFingerprinter')
    hybridizationfingerprinter = HybridizationFingerprinter()
    molecule = smilesParser.parseSmiles(smiles)
    fingerprint = hybridizationfingerprinter.getFingerprint(molecule)
    length = hybridizationfingerprinter.getSize()
    fingerprint_list = JavaToPython(fingerprint)
    fingerprint_dict = {}
    for i in range(length):
        if i in fingerprint_list:
            fingerprint_dict.setdefault(i, 1)
        else:
            fingerprint_dict.setdefault(i, 0)

    vec_list = list(fingerprint_dict.values())
    print(length)
    vec_nparray = np.array(vec_list)
    return vec_nparray


if __name__ == '__main__':
    smiles = 'O=C1C(C2=C(O)C=C(N(C(C)CC)CCC)C=C2O)=C([O-])/C1=C(C(O)=C/3)\C(O)=CC3=[N+](CCC)\C(C)CC'
    startJVM(getDefaultJVMPath(), "-ea")
    #print(1)
    # for i in range(10):
    #     print(GetCDKMACCSFingerPrint(smiles).tolist())
    #print(GetCDKExtendedFingerprint(smiles).tolist())
    print(GetCDKHybridizationFingerprint(smiles).tolist())
    #print(GetCDKPubchemFingerprint(smiles).tolist())
    shutdownJVM()