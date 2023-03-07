import os
from bs4 import BeautifulSoup
import inflect
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

p=inflect.engine()
chrome_options = Options()
c_options = Options()
chrome_options.add_extension('fdm.crx')
chrome_options.add_experimental_option("detach", True)
c_options.add_argument("window-size=1920x1080")
c_options.add_argument('--headless')
c_options.add_argument('--disable-gpu')
x=Service('C:\Program Files (x86)\chromedriver.exe')
web=[]
list3=[]
list4=[]
list5=[]

def search():
    site_name="https://animepahe.com/"
    global sea, fe,le,link, resol
    sea=input("What do you want to search: ")
    resol=input("In which resolution: ")
    stor=input("Do you want to know the storage: ")
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
    driver=webdriver.Chrome(options=chrome_options, service=x)
    driver.get(ani_url)
    dezz=driver.find_element(By.NAME, 'q')
    dezz.send_keys(sea)
    driver.get(link)
    return link

def daily_anime(ani_url):
    soup=BeautifulSoup(driver.page_source,"lxml")
    span=soup.find_all("span",class_='episode-title')
    did=soup.find_all("div", class_='episode-number')

    for pi in did:
        print(pi.text,"\n")

def search2(ulink):
    global soup, dix, sp, eps_num, nextin
    wait=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'episode-number')))
    wait2=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'episode-snapshot')))
    soup=BeautifulSoup(driver.page_source,'lxml')
    dix=soup.find_all("div",class_="episode-number")
    sp=soup.find_all("div",class_="episode-snapshot")
    driver.implicitly_wait(10)
    nextin=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="page-link next-page"]')))
    eps_num=[]
    driver.implicitly_wait(10)
    for num1 in dix:  
        ep_num=num1.text.replace("Episode","")
        eps_num.append(ep_num.strip())

def second_page():
    for num in range(fe,le+1):
        i=0
        global new_link
        while i!=1:
            search2(first_page())
            if num<int(eps_num[-1]) and str(num) in eps_num and  num>30:
                    num2=num-(30*(num//30))
                    new_link="https://animepahe.com"+sp[num2-1].a['href']  
                    web.append(new_link)
                    i=1
            elif num<int(eps_num[-1]) and str(num) in eps_num and  num<30:
                    new_link="https://animepahe.com"+sp[num-1].a['href']
                    web.append(new_link)
                    i=1
            else:
                nextin.click()
                i=0
        
    else:
        for x in web:
            driver.get(x)
            list3=[]
            if stor == "yes":   
                storage=requests.get(x).text
                bread=BeautifulSoup(storage,"lxml")
                dropdown=bread.find_all("div",id="pickDownload" )
                #print(dropdown)
                for l in dropdown:
                    if resol in str(l):
                        link=l.a.text
                        list3.append(link)
                    else:
                        pass
                print(list3)
                for stor in list3: 
                    #print(stor)  
                    for x in stor:
                        if x=="(":
                            break
                        else: 
                            stor=stor.replace(x,"",1)
                    list4.append(stor.strip()+"f")
                    print(list4)
                    for mn in list4:
                        for x in mn:
                            if x.isdigit():
                                pass
                            else:
                                mn=mn.replace(x,"",1)
                    list5.append(int(mn))
                stor="yes"
                resol = resol
        print(list5)
        print("The total storage is",sum(list5),"MB")
        last_page(third_page(x))

def third_page(ulink):
    driver.get(ulink)
    soup=BeautifulSoup(driver.page_source,'lxml')
    dip=soup.find("div", class_='dropdown-menu',id='pickDownload')
    res=dip.find_all("a")
    link=''
    
    for l in res:
        if resol in str(l):
            link=l['href']
        else:
            pass
    if link=='':
        print("No resolution")
    else:
        pass
    driver.get(link)
    wait=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Continue')))
    soup=BeautifulSoup(driver.page_source,"lxml")
    pahe=soup.find("div",class_="col-sm-6")
    link2=pahe.a['href']
    return link2

def last_page(ulink):
    driver.get(ulink)
    button1=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]')))
    driver.execute_script("arguments[0].click();", button1)
first_page(search())
second_page()
sleep(10)
driver.close()