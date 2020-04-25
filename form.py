# -*- coding: utf-8 -*-
# coding: utf-8
# @Author  : WeiXin
# 忽略版本警告
import warnings

warnings.filterwarnings('ignore')

from wtforms import Form, StringField, SubmitField, SelectField, SelectMultipleField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Required

class PredictForm(Form):
    smiles = StringField('SMILES')
    al_fingerprint = SelectField('选择算法', choices=[('0', 'Regression-RF-Morgan-PCE'),
                                                  ('1', 'Regression-SVM-Hybridization-PCE'), ('2', 'Regression-GBDT-Daylight-PCE')])
    # fingerprint = SelectField('选择指纹', choices=[('0', 'RDKIT-DaylightFingerprint'),
    #                                            ('1', 'RDKIT-TopologicalTorsionFingerprint'), ('2', 'RDKIT-AtomPairFingerprint'), ('3', 'RDKIT-EstateFingerprint'),
    #                                            ('4', 'RDKIT-RDKFingerprint'), ('5', 'RDKIT-MACCSFingerprint'), ('6', 'RDKIT-MorganFingerprint'),
    #                                            ('7', 'CDK-MACCSFingerprint'), ('8', 'CDK-PubchemFingerprint'), ('9', 'CDK-ExtendedFingerprint'),
    #                                            ('9', 'CDK-HybridizationFingerprint')])
    result = TextAreaField()
    submit = SubmitField('提交')

class ConvertForm(Form):
    smiles = StringField('SMILES')
    fingerprint = SelectField('选择指纹', choices=[('0', 'RDKIT-DaylightFingerprint'),
                                               ('1', 'RDKIT-TopologicalTorsionFingerprint'),
                                               ('2', 'RDKIT-AtomPairFingerprint'), ('3', 'RDKIT-EstateFingerprint'),
                                               ('4', 'RDKIT-RDKFingerprint'), ('5', 'RDKIT-MACCSFingerprint'),
                                               ('6', 'RDKIT-MorganFingerprint'),
                                               ('7', 'CDK-MACCSFingerprint'), ('8', 'CDK-PubchemFingerprint'),
                                               ('9', 'CDK-ExtendedFingerprint'),
                                               ('9', 'CDK-HybridizationFingerprint')])
    file = FileField('file')
    submit = SubmitField('Submit')

#
# pf = PredictForm()
# print(pf.smiles())