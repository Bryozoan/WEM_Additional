# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

#  These are so I don't get board
#  hopfully they are also helpful

def Notification_Starting_function():

    print("Starting Script")
    print("starting function")


def Notification_web_browswerstarting():

    print("Starting firefox")
    print("going to the utah government website (instert url)")
    print("--> download and property loading remaining")


Notification_Starting_function()


def updateWells():

    # this is the path for firefox driver
    path = r'C:\Users\duckm\Documents\Coding\geckodriver.exe'
    driver = webdriver.Firefox(executable_path=path)

    def findElement(XPATH):
        find = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, XPATH)))
        return find


    driver.get(r'https://opendata.gis.utah.gov/datasets/utahDNR::utah-oil-and-gas-wells-paths/explore?location=39.512024%2C-111.338665%2C-1.00')
    driver.maximize_window()
    Notification_web_browswerstarting()
    time.sleep(20)

    #  define the variables that make will download the file
    downloadPage = findElement(r'/html/body/div[6]/div[2]/div/div[1]/div[2]/div/div/nav/div/div/div/button[3]')
    downloadPage.click()
    print("Going to download page")


    # toggleSwitch = findElement(r'/html/body/div[6]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/calcite-switch')
    # toggleSwitch()
    print("requesting newest information")

    getFile = findElement(r'/html/body/div[6]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[5]/hub-download-card//calcite-card/div/calcite-dropdown/calcite-button')
    getFile.click()
    latestData = findElement(r'/calcite-card/div/calcite-dropdown/calcite-dropdown-group/calcite-dropdown-item[1]/span')
    latestData.click()
    print("Downloading most recent shapefile")


updateWells()

print("done")
