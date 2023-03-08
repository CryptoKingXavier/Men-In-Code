import os
from bs4 import BeautifulSoup
from web3 import second_page
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
os.environ['PATH']+= r'C:\Program Files (x86)\chromedriver.exe'
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
x=Service('C:\Program Files (x86)\chromedriver.exe')

driver=webdriver.Chrome(options=chrome_options, service=x)
driver.get("https://animepahe.com/")
#driver.implicitly_wait(100)
#butto=driver.find_elements(By.CLASS_NAME,'episode-wrap col-12 col-sm-4')

def first_page():
    dezz=driver.find_element(By.NAME, 'q')
    sea=input("What do you want to search: ")
    dezz.send_keys(sea)
    sleep(5)
    search_results=driver.find_element(By.CLASS_NAME,'search-results')
    plane= search_results.find_elements(By.TAG_NAME, 'a')
    #print("OuterHTML:",plan.get_attribute("outerHTML"))
    #print("")
    count=0
    for plan in plane:
        count+=1
        if len(plane)==count:
            print('This is the last result\n')
        else:
            print('This is the %s result'%(p.ordinal(count)))
        nice=plan.get_attribute("outerHTML")
        soup=BeautifulSoup(nice,"lxml")
        link="https://animepahe.com"+soup.find('a')['href']
        print(soup.text,"\n")
        aniname=soup.text
        confirm=input("Is it %s:\n"%(aniname))
        if str(confirm)=="yes":
            driver.get(link)
            break
        else:
            pass

second_page()

sleep(10)
driver.close()

#driver.implicitly_wait(100)
#print(driver.page_source)
