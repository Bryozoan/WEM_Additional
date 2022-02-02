# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 11:52:01 2022

@author: Accounting
"""

#This program is designed to update the backround wells on the main map. After 
#you run this program you will need to copy and paste the attibutes from the old
#'OilandGasWells files in q. 

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

# These are notifications so I don't get board waiting form the computer 
# to do anything
def Notification(message):
    #based on input, the message output will be different 
    if message == 'start1':
        print("Starting program")
    elif message == 'starting2':
        print("Starting Script")
    elif message == 'Browser':
        print("Starting Browser")
    elif message == 'Browswer1':
        print("Going to the Utah government website")
    elif message == 'download':
        print("--> Downloading, Please waite")
    else :
        print("spelling wrong")
 
#Setup:
#this is the path from the web-driver
path = r'\\WEM-MASTER\Working Projects\WEMU Leasing\Python Codes\Python Code\chromedriver.exe'
driver = webdriver.Chrome(path)


def updateWells():
            
    def findElement(XPATH):
        find = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH)))
        return find
    
    #message in console
    Notification('Starting program')
    driver.get(r'https://opendata.gis.utah.gov/datasets/utahDNR::utah-oil-and-gas-wells-paths/explore?location=39.512024%2C-111.338665%2C-1.00')
    Notification('Browser')
    time.sleep(20)
    driver.maximize_window()
    time.sleep(5)
    
    downloadPage = findElement(r'//*[@id="ember78"]/div/button[3]')
    downloadPage.click()
    time.sleep(5)
    
    #togSwitch = findElement(r'//*[@id="ember47"]/div/div/div[1]/div/div/div[2]/div/calcite-switch//div')
    #togSwitch.click()
    
    downLdOpts = findElement(r'//*[@id="ember47"]/div/div/div[1]/div/div/div[5]/hub-download-card//calcite-card/div/calcite-dropdown/calcite-button')
    downLdOpts.click()
    
    downLdData = findElement(r'//*[@id="ember47"]/div/div/div[1]/div/div/div[5]/hub-download-card//calcite-card/div/calcite-dropdown/calcite-dropdown-group/calcite-dropdown-item[1]//div')
    downLdData.click()
    Notification('download')
    time.sleep(50)

    
updateWells()
  