#Changes the Windows 10 background to the Bing Image of the Day
import requests, urllib, ctypes
import xml.etree.ElementTree as ET
#Loads url's content into a text file: res.text
url = 'https://www.bing.com/HPImageArchive.aspx?format=html&idx=0&n=2&mkt=en-u'
res = requests.get(url)
#Error checking
res.raise_for_status()
#Parsing url from a text file
root = ET.fromstring(res.text)
#Assembles url from the list: root
imageURL = 'https://www.bing.com' + root[0][3].text
#Saves
savePath = "C:\\Users\\stran\\OneDrive\\Documents\\Wallpaper\\BingWall.jpg"
urllib.request.urlretrieve(imageURL, savePath)
ctypes.windll.user32.SystemParametersInfoW(20 , 0, savePath ,3)


