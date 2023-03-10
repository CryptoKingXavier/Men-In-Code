from dataclasses import replace
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
x=Service("C:\Program Files (x86)\chromedriver.exe")
pop=input("What resolution: ")
list3=[]

driver=webdriver.Chrome(options=chrome_options, service=x)
def third_page(ulink="https://animepahe.com/play/1054a99c-7d03-b114-15ae-291da1ee40fc/25930e44622252148dd21525d309fea1e8005c24477e0d1f5dc69461e362c7c5"):
    driver.get(ulink)
    soup=BeautifulSoup(driver.page_source,"lxml")
    dip=soup.find("div", class_='dropdown-menu',id='pickDownload')
    res=dip.find_all("a")
    #print(dip)
    link=''
    for l in res:
        if pop in str(l):
            print("Yasss")
            link=l['href']
        else:
            pass
    driver.get(link)
    #sleep(2)
    wait=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Continue')))
    soup=BeautifulSoup(driver.page_source,"lxml")
    pahe=soup.find("div",class_="col-sm-6")
    link2=pahe.a['href']
    print(link2)
    driver.get(link2)
    return link2

third_page()
#sleep(10)
driver.close()
