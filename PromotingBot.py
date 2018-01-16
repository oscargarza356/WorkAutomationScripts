from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# LoginScript-----------------------------------------------------------------------------------------------------------------------------
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


counter = 0

text = 'Hello we are a brand new store selling hype accessories we will be ' \
           'selling all kinds of products, from Supreme to Off-White ,' \
           'at Centurion Store we are always striving to bring you the best items and at the best price.'+ u'\uD83D\uDD25' + u'\uD83D\uDD25' + u'\uD83D\uDD25'

# Comment Script-------------------------------------------------------------------------------------------------------
def commentInInstagramPostNumber(webPageLink, postNumber):
    browser.get(webPageLink)
    time.sleep(1)

    post = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div[1]/div[1]/div["+str(postNumber)+"]/a")
    post.click()
    time.sleep(2)

    clickComment = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/article/div[2]/section[1]/a[2]')
    clickComment.click()
    time.sleep(1)

    JS_ADD_TEXT_TO_INPUT = """
          var elm = arguments[0], txt = arguments[1];
          elm.value += txt;
          elm.dispatchEvent(new Event('change'));
          """

    writeComment = browser.find_element_by_xpath(
        '/html/body/div[4]/div/div[2]/div/article/div[2]/section[3]/form/textarea')

    browser.execute_script(JS_ADD_TEXT_TO_INPUT, writeComment, text)
    writeComment.send_keys(" ")
    time.sleep(3)

    writeComment.send_keys(Keys.RETURN)
    time.sleep(30)

postNumber = 1

webPagesForScripts = [
                      'https://www.instagram.com/worldstar/', 'https://www.instagram.com/quavohuncho/',
                      'https://www.instagram.com/asaprocky/', 'https://www.instagram.com/iamcardib/',
                      'https://www.instagram.com/liluzivert/', 'https://www.instagram.com/lilpump/',
                      'https://www.instagram.com/hypebeast/'  ,'https://www.instagram.com/smokepurpp/',
                      'https://www.instagram.com/kimkardashian/','https://www.instagram.com/justinbieber/']

random.shuffle(webPagesForScripts)

for webPage in webPagesForScripts:
    commentInInstagramPostNumber(webPage,postNumber)