from dataclasses import replace
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
x=Service("C:\Program Files (x86)\chromedriver.exe")

driver=webdriver.Chrome(options=chrome_options, service=x)
driver.get("https://animepahe.com/")

soup=BeautifulSoup(driver.page_source,'lxml')
def daily_anime():
    span=soup.find_all("span",class_='episode-title')
    did=soup.find_all("div", class_='episode-number')
    #ep_num="let's say 3 fkek4 23"
    #eps_num=""
    #for el in ep_num:
    #    if any(i.isdigit() for i in el):
    #        print(el)
    #    else:
    #        el=""
    #    eps_num+=el
    #print(eps_num)

    for pi in did:
        print(pi.text,"\n")
sleep(10)
driver.close()