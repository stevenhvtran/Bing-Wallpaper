import bs4, selenium, ctypes, requests, time, urllib.request
from selenium import webdriver  #This is required as webdrive is a module in a module
time.sleep(3)
url = 'https://www.bing.com'    #Designates URL being used
driver = webdriver.Chrome()     #Selenium uses Chrome to execute further commands
driver.get(url)                 #Opens the webpage in Chrome
time.sleep(1)                 #Allows for javascript crap to load

elem = driver.find_element_by_id('bgDiv')
URL = elem.value_of_css_property('background-image')
print(URL[5:-2])
driver.quit()
urllib.request.urlretrieve(URL[5:-2], "C:\\Users\\stran\\OneDrive\\Documents\\Automate The Boring Stuff\\BingWall.jpg")
ctypes.windll.user32.SystemParametersInfoW(20 , 0, "C:\\Users\\stran\\OneDrive\\Documents\\Automate The Boring Stuff\\BingWall.jpg" ,0)

