import requests
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import urllib.request   
from bs4 import BeautifulSoup
from time import sleep

x=Service('C:\Program Files (x86)\chromedriver.exe')
driver=webdriver.Chrome(service=x)
driver.get("https://animepahe.com/")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(5)
src=[]
mom=requests.get("https://animepahe.com/").text
soup=BeautifulSoup(driver.page_source,"lxml")
img=soup.find_all("img",class_='lazyloaded')

for i in img:
    src.append(str(i['src']))


for a in range(10):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'MyApp/1.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(str(src[a]),"images/anipics{}.jpg".format(a))
