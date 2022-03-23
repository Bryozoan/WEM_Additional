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
    

#Leasholds
# this will take the Working interest file from ILM and convert it into a CSV 
# for QGIS.
def leaseLabel(ILMfile):
    #Import the data
    tractLea = pd.read_excel(ILMfile, sheet_name="Well-Bore Only",
                             header=5)
    #Remove the tract number so that that they can be summed by section
    tractLea['Section'] = tractLea['Tract Number'].map(lambda x: str(x)[2:-4])
    tractLea = tractLea.dropna(axis=0, subset=['Tract Number'])
    
    
    WEMI = pd.DataFrame()    
    WEMI['Section'] = tractLea.Section
    WEMI['Min. Net Acres'] = tractLea['TRACT Min. Net Acres']
    WEMI['WEM Uintah, LLC Ownership'] = tractLea['WEM Uintah, LLC Ownership']
    WEMI = WEMI.dropna(axis=0, subset=['WEM Uintah, LLC Ownership'])
    WEMI['WEM1 Leasehold'] = WEMI['WEM Uintah, LLC Ownership']*WEMI['Min. Net Acres']
    WEMI = WEMI[WEMI != 0].dropna(axis=0)
    WEMI = WEMI.groupby(["Section"])['WEM1 Leasehold'].sum().reset_index()
    
    WEM2 = pd.DataFrame()    
    WEM2['Section'] = tractLea.Section
    WEM2['Min. Net Acres'] = tractLea['TRACT Min. Net Acres']
    WEM2['WEM Uintah II, LLC Ownership'] = tractLea['WEM Uintah II, LLC Ownership']
    WEM2 = WEM2.dropna(axis=0, subset=['WEM Uintah II, LLC Ownership'])
    WEM2['WEM2 Leasehold'] = WEM2['WEM Uintah II, LLC Ownership']*WEM2['Min. Net Acres']
    WEM2 = WEM2[WEM2 != 0].dropna(axis=0)
    WEM2 = WEM2.groupby(["Section"])['WEM2 Leasehold'].sum().reset_index()
    
    WEM3 = pd.DataFrame()    
    WEM3['Section'] = tractLea.Section
    WEM3['Min. Net Acres'] = tractLea['TRACT Min. Net Acres']
    WEM3['WEM Uintah III, LLC Ownership'] = tractLea['WEM Uintah III, LLC Ownership']
    WEM3 = WEM3.dropna(axis=0, subset=['WEM Uintah III, LLC Ownership'])
    WEM3['WEM3 Leasehold'] = WEM3['WEM Uintah III, LLC Ownership']*WEM3['Min. Net Acres']
    WEM3 = WEM3[WEM3 != 0].dropna(axis=0)
    WEM3 = WEM3.groupby(["Section"])['WEM3 Leasehold'].sum().reset_index()
    
    WEMI.to_csv(CSVfile+r'\WEM1Leasehold.csv')
    WEM2.to_csv(CSVfile+r'\WEM2Leasehold.csv')
    WEM3.to_csv(CSVfile+r'\WEM3Leasehold.csv')
    
    return(tractLea, WEMI, WEM2, WEM3)


TractLea, WEM1, WEM2, WEM3 = leaseLabel(CSVfile+r'\Working Interest Detail.xlsx')

#tractOwn, QData, dSize, WEMOwn, WEMIOwn, WEMIIOwn, WEMIIIOwn = labels(CSVfile+r'\Tract Ownership List.xlsx')
