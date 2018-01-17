from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# Login Script--------------------------------------------------------------------------------------------------
chromedriver = "C:\\Users\\oscar\\Desktop\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.instagram.com/accounts/login/?hl=en')
time.sleep(2)

account = browser.find_element_by_name("username")
account.send_keys("centurionstoreus")
time.sleep(1)

passw = browser.find_element_by_name("password")
passw.send_keys("royal356")
time.sleep(1)

loginButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/span/button")
loginButton.click()
time.sleep(5)


# Following Script---------------------------------------------------------------------------------------------------
flag = 0

def followUsers(webPageLink,postOfwebpage):
    global flag

    browser.get(webPageLink)
    time.sleep(4)

    post = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div[1]/div[1]/div["+str(postOfwebpage)+"]/a")
    post.click()
    time.sleep(3)

    likeButton = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/article/div[2]/section[2]/div/a")
    likeButton.click()
    time.sleep(2)


    counter = 1
    if flag % 3 != 0:
        while counter < 15:
            followButton = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/article/div[2]/div[2]/ul/div/li["+str(counter)+"]/div/div[2]/span/button")
            followButton.click()
            counter += 1
            time.sleep(2)

    flag += 1
    time.sleep(30)


postNumber = 1

webPagesForScripts = ["https://www.instagram.com/kanyew.est/", 'https://www.instagram.com/supreme_leaks_news/',
                      'https://www.instagram.com/supremenewyork/',
                      'https://www.instagram.com/supcommunity/?hl=en',"https://www.instagram.com/kanyew.est/",
                      'https://www.instagram.com/supreme__hustle/','https://www.instagram.com/complex/',
                      'https://www.instagram.com/worldstar/', 'https://www.instagram.com/quavohuncho/',
                      'https://www.instagram.com/asaprocky/', 'https://www.instagram.com/iamcardib/',
                      'https://www.instagram.com/liluzivert/', 'https://www.instagram.com/lilpump/',
                      'https://www.instagram.com/lilpump/','https://www.instagram.com/smokepurpp/',
                      'https://www.instagram.com/kimkardashian/','https://www.instagram.com/justinbieber/']

random.shuffle(webPagesForScripts)

for webPage in webPagesForScripts:
    followUsers(webPage, postNumber)