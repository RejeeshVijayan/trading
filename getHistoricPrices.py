#!/usr/local/bin/python3
from selenium import webdriver
import sys
import time
import os

#create a directory for saving the csv historic data files
csvPath = os.getcwd() + "/tmp"
try:
    os.stat(csvPath)
except:
    os.mkdir(csvPath)

#FIXME arguments parsing
symbols = sys.argv[1:-2]
#fromDate = '01-08-2016'
#toDate   = '01-08-2017'
fromDate  = sys.argv[-2]
toDate    = sys.argv[-1]

# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir',csvPath)
profile.set_preference('browser.download.folderList',2)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk',"application/csv")

#open Firefox
driver = webdriver.Firefox(profile)

for symbol in symbols:
    #FIXME Clean Up existing data for this stock
    print("INFO: Fetching Historic data for "+symbol)
    driver.get("https://www.nseindia.com/products/content/equities/equities/eq_security.htm")
    elem = driver.find_element_by_id("symbol") #Fill in Stock symbol
    elem.send_keys(symbol)
    elem = driver.find_element_by_id("rdDateToDate") #Radio button to feed the time period.
    elem.click()
    elem = driver.find_element_by_id("fromDate") # Form - from date
    elem.send_keys(fromDate)
    elem = driver.find_element_by_id("toDate")   # Form - to date
    elem.send_keys(toDate)
    driver.find_element_by_id("get").click()     # Click get button
    time.sleep(2)                                # Allow some time for the website to populate teh data
    elem = driver.find_element_by_xpath(r'''//*[@id="historicalData"]/div[1]/span[2]/a''').click() #click the download link

driver.close()

