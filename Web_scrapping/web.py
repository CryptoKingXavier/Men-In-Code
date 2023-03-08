import requests
import os
from web3 import web, second_page
from bs4 import BeautifulSoup
import inflect
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import soupsieve

p=inflect.engine()
chrome_options = Options()
c_options = Options()
chrome_options.add_extension('fdm.crx')
chrome_options.add_experimental_option("detach", True)
c_options.add_argument("window-size=1920x1080")
c_options.add_argument('--headless')
c_options.add_argument('--disable-gpu')
x=Service('C:\Program Files (x86)\chromedriver.exe')

def search():
    site_name="https://animepahe.com/"
    global sea, fe,le,link, resol
    sea=input("What do you want to search: ")
    resol=input("In which resolution: ")
    if resol =="720" or resol=="720p" or resol=="1080" or resol=="1080p" or resol=="360p" or resol=="360":
        pass
    else:
        exit()
    fe=int(input("What is the first episode to be downloaded: "))
    le=int(input("What is the last episode to be downloaded: "))
    driver=webdriver.Chrome(options=c_options, service=x)  
    driver.get(site_name)
    driver.implicitly_wait(10)
    d=driver.find_element(By.NAME, 'q')
    d.send_keys(sea)
    soup=BeautifulSoup(driver.page_source,'lxml')
    search_results=driver.find_element(By.CLASS_NAME,'search-results')
    plane= search_results.find_elements(By.TAG_NAME, 'a')
    count=0
    for plan in plane:
        count+=1
        if len(plane)==count:
            print('\nThis is the last result')
        else:
            print('\nThis is the %s result'%(p.ordinal(count)))
        nice=plan.get_attribute("outerHTML")
        soup2=BeautifulSoup(nice,"lxml")
        link=site_name+soup2.find('a')['href']
        aniname=soup2.text
        confirm=input("Is it %s:\n"%(aniname))
        if str(confirm)=="yes":
            driver.get(link)
            break
        else:
            pass  
    return site_name
def first_page(ani_url):
    global driver
    stor=input("Do you want to know the storage space")
    driver=webdriver.Chrome(options=chrome_options, service=x)
    driver.get(ani_url)
    dezz=driver.find_element(By.NAME, 'q')
    dezz.send_keys(sea)
    #driver.get(link)
    return link
first_page(search())
