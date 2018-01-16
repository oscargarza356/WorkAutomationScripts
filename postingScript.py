from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#itemTitle  = input("Title of item")

#itemBrand  = input("item Brand")

#itemDescription = (itemTitle, " in excellent conditions.\n""Will ship within a day of purchase!\n""If you have any questions feel free to ask me." )


chromedriver = "C:\\Users\\oscar\\Desktop\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)

#Login Script ---------------------------------------------------------------------------------


browser.get('https://www.brisksale.com/signin')

time.sleep(1)
username = browser.find_element_by_xpath("/html/body/div[7]/div/div/div/form/div[1]/div/input")
password = browser.find_element_by_xpath("/html/body/div[7]/div/div/div/form/div[2]/div/input")

username.send_keys("arturo35689@hotmail.com")
password.send_keys("manto356")

login = browser.find_element_by_xpath("/html/body/div[7]/div/div/div/form/div[3]/div/button").click()

#Selling Script ---------------------------------------------------------------------------------

browser.get("https://www.brisksale.com/post-listing-v2/#/")

time.sleep(1)
title =  browser.find_element_by_name("title")
title.send_keys("itemTitle")

time.sleep(0.1)

brand =  browser.find_element_by_name("brand")
brand.send_keys("itemBrand")

time.sleep(0.1)

description =  browser.find_element_by_name("description")
description.send_keys("itemDescription")

time.sleep(0.5)

category1 = browser.find_element_by_xpath("//*[@id='listing-step01-block']/form/div/div[4]/div[3]/div[1]/select")
category1.click()
category1.send_keys("fashion")
category1.click()





time.sleep(0.1)

category1 = browser.find_element_by_name("category_2")
category1.click()
category1.send_keys("clothing")
category1.click()


time.sleep(0.1)

category1 = browser.find_element_by_name("category_3")
category1.click()
category1.send_keys("men")
category1.click()

time.sleep(0.1)


condition = browser.find_element_by_xpath("//*[@id='listing-step01-block']/form/div/div[4]/div[4]/div[1]/div/label[2]")
condition.click()

tagButton = browser.find_element_by_xpath("//*[@id='listing-step01-block']/form/div/div[4]/div[5]/div[1]/div/span/button")
tagsDescription = browser.find_element_by_xpath("//*[@id='listing-step01-block']/form/div/div[4]/div[5]/div[1]/div/input")
tagsDescription.send_keys("supreme")
tagButton.click()
tagsDescription.send_keys("urban")
tagButton.click()
tagsDescription.send_keys("hype")
tagButton.click()
tagsDescription.send_keys("hypebeast")
tagButton.click()

quantity = browser.find_element_by_xpath("//*[@id='listing-step01-block']/form/div/div[4]/div[6]/div/input")
quantity.send_keys(5)

time.sleep(35)

submitButton = browser.find_element_by_xpath("//*[@id='listing-step01-block']/form/div/div[4]/div[9]/div/input")
submitButton.click()

time.sleep(0.1)


price  = browser.find_element_by_xpath("//*[@id='listing-step02-block']/form/div/div/div[1]/div[1]/input")
price.send_keys("1")

time.sleep(0.1)


comission = browser.find_element_by_xpath("//*[@id='listing-step02-block']/form/div/div/div[2]/div[1]/input")
comission.send_keys("1")

time.sleep(0.1)

sale = browser.find_element_by_xpath("//*[@id='listing-step02-block']/form/div/div/div[5]/div[2]/input")
sale.send_keys("10")