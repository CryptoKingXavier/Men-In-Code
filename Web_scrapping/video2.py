import base64
import requests
import shutil
from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import urllib.request   
from bs4 import BeautifulSoup
from time import sleep

x=Service('C:\Program Files (x86)\chromedriver.exe')
driver=webdriver.Chrome(service=x)
driver.get("https://animepahe.com/play/75f4d33d-1a9a-728f-82e9-8d1bb35f37d0/a92cde122223e1e2ce2e117a458166782d25fbcf06996fe39a9adfc0c9b50e4d")
sleep(2)
iframe=driver.find_element(By.XPATH, '//iframe[@class="embed-responsive-item"]')
but=driver.find_element(By.XPATH, '//div[@class="reload"]')
driver.execute_script("arguments[0].click();", but)
driver.switch_to.frame(iframe)
sleep(7)
JS_get_network_requests = "var performance = window.performance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
network_requests = driver.execute_script(JS_get_network_requests)
m3u8_url=""
#print(network_requests)
for n in network_requests:
    if ".m3u8" in n["name"]: 
        m3u8_url=n["name"]
print(m3u8_url)
session=requests.Session()
opener = {'User-Agent': 'Mozilla/5.0'}
req=session.get(m3u8_url, headers=opener)
print(req.content)