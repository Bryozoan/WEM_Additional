# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:29:28 2022

@author: GISUser
"""

#this code is meant to replace the r code peter wrote.


#import packages
import pandas as pd
import numpy as np

#######################
#testingbox
ILMfile = r'C:\Users\GISUser\Downloads\NewLabelsTest\Tract Ownership List.xlsx'

CSVfile = r'C:\Users\duckm\Downloads\QGIStest'

#######################


#function Ownership Labels:
def labels(ILMfile):
    tractOwn = pd.read_excel(ILMfile, sheet_name="TractOwnershipReport",
                             header=5)
    tractOwn['Section'] = tractOwn['Tract Number'].map(lambda x: str(x)[:-4])
    tractOwn = tractOwn.dropna(axis=0, subset=['Tract Number'])
    
    QData = pd.DataFrame()
    QData['Twn Rng Sec'] = tractOwn.Section.unique()
    dSize = len(QData.index)
    
    QData.insert(1,'WEM I Ownership',0)
    
    WEMOwn = tractOwn.groupby(["Section","Name"])['Net Mineral Acres'].sum().reset_index()
    WEMOwn['Section'] = WEMOwn['Section'].str[2:]
    #WEMIOwn = WEMOwn.where(tractOwn['Name'].eq("WEM Uintah, LLC"))
    WEMIOwn = WEMOwn.loc[(WEMOwn["Name"] == "WEM Uintah, LLC")]
    WEMIIOwn = WEMOwn.loc[(WEMOwn["Name"] == "WEM Uintah II, LLC")]
    WEMIIIOwn = WEMOwn.loc[(WEMOwn["Name"] == "WEM Uintah III, LLC")]
    
    WEMIOwn.to_csv(CSVfile+r'\WEM1Labels.csv')
    WEMIIOwn.to_csv(CSVfile+r'\WEM2Labels.csv')
    WEMIIIOwn.to_csv(CSVfile+r'\WEM3Labels.csv')
    
    
# =============================================================================
#     for i in range(dSize):
#         
#         WEMOwn = tractOwn.groupby(["Section","Name"])['Net Mineral Acres'].sum().reset_index()
#         QData['WEM I Ownership'] = WEMOwn
#         
#         #lists = tractOwn[['Net Mineral Acres']].sum(axis=0).where(tractOwn['Net Mineral Acres']==QData.at[1,'Twn Rng Sec'])
#         #QData.iloc[i]['WEM I Ownership'] = tractOwn[['Net Mineral Acres']].sum(axis=(0)).where(tractOwn['Section']==QData.at[i,'Twn Rng Sec'])
# 
# =============================================================================
                                        
    return(tractOwn, QData, dSize, WEMOwn, WEMIOwn, WEMIIOwn, WEMIIIOwn)
    
    
tractOwn, QData, dSize, WEMOwn, WEMIOwn, WEMIIOwn, WEMIIIOwn = labels(CSVfile+r'\Tract Ownership List.xlsx')
