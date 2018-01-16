from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


name = input("Addressee full name\n")

print("Please enter the address of the buyer")
buyerInfo = []
counter = 0;
while counter < 3:
    try:
        line = input("")
    except EOFError:
        break
    buyerInfo.append(line)
    counter += 1

streetAddress, cityState, postal = buyerInfo
print(buyerInfo)

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
          'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
          'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
          'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
          'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
          'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
          'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
          'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
          'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
city = ''
state = ''
for state in states:
    if state in cityState:
        city = cityState.split(state)[0]
        break

postal = postal.split('-')[0]
print(streetAddress,"\n"+city, "\n"+state,"\n"+postal)


chromedriver = "C:\\Users\\oscar\\Desktop\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.paypal.com/login')

email = browser.find_element_by_id("email")
email.clear()
email.send_keys("agmirazo@hotmail.com")

browser.find_element_by_id("btnNext").click()

browser.implicitly_wait(1000)

password = browser.find_element_by_id("password")
password.send_keys("oscar3567")

browser.find_element_by_id("btnLogin").click()

browser.get('https://www.paypal.com/shiplabel/create/')


time.sleep(3)

customerName = browser.find_element_by_id("addresseeName")
customerName.send_keys(name)
time.sleep(0.5)


address = browser.find_element_by_id("street1")
address.send_keys(streetAddress)
time.sleep(0.5)


cityBuy = browser.find_element_by_id("city")
cityBuy.send_keys(city)
time.sleep(0.5)


stateBuy = browser.find_element_by_id("stateOrProvince")
stateBuy.send_keys(state)
time.sleep(0.5)


postalCode = browser.find_element_by_id("postalCode")
postalCode.send_keys(postal)
time.sleep(0.5)


browser.find_element_by_id("SaveToAddress").click()


delivery = browser.find_element_by_id("service-type")
delivery.send_keys("first")
time.sleep(0.5)


shippingWeight = browser.find_element_by_id("weightGMorOZ")
shippingWeight.clear()
shippingWeight.send_keys("5")
time.sleep(0.5)

browser.find_element_by_id("calculateShippingCost").click()