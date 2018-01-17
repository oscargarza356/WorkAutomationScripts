from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# Login Script--------------------------------------------------------------------------------------------------
chromedriver = "C:\\Users\\oscar\\Desktop\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)
browser.get('https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&UsingSSL=1&pUserId=&co_partnerId=2&siteid=0&ru=http%3A%2F%2Fmy.ebay.com%2Fws%2FeBayISAPI.dll%3FMyEbayBeta%26MyEbay%3D%26gbh%3D1%26guest%3D1&pageType=3984')
time.sleep(2)

username = browser.find_element_by_xpath('//*[@id="userid"]')
username.send_keys('centurionstore')

password = browser.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('yeahyeah123')

loginButton = browser.find_element_by_xpath('//*[@id="sgnBt"]')
loginButton.click()
time.sleep(2)

browser.get('https://www.ebay.com/sh/ord/?filter=status:AWAITING_SHIPMENT')
time.sleep(2)

bulkShip = browser.find_element_by_xpath('//*[@id="grid-table-bulk-checkbox"]')
bulkShip.click()
time.sleep(0.2)

shippingButton = browser.find_element_by_xpath('//*[@id="gridSummary-wrapper-id-w9"]/button')
shippingButton.click()
time.sleep(0.2)

printButton = browser.find_element_by_xpath('//*[@id="printInvoice"]')
printButton.click()
time.sleep(2)

continueButton = browser.find_element_by_xpath('//*[@id="frmSubmit"]/table/tbody/tr[6]/td/input[8]')
continueButton.click()
time.sleep(2)