import os
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
    global sea, user,link
    sea=input("What do you want to search: ")
    user=input("What episode are you looking for: ")
    #print(sea)
    driver=webdriver.Chrome(options=c_options, service=x)  
    driver.get(site_name)
    driver.implicitly_wait(10)
    d=driver.find_element(By.NAME, 'q')
    #print(d,"\n",d.get_attribute("outerHTML"))
    d.send_keys(sea)
    soup=BeautifulSoup(driver.page_source,'lxml')
    search_results=driver.find_element(By.CLASS_NAME,'search-results')
    plane= search_results.find_elements(By.TAG_NAME, 'a')
    count=0
    for plan in plane:
        count+=1
        if len(plane)==count:
            print('This is the last result\n')
        else:
            print('This is the %s result'%(p.ordinal(count)))
        nice=plan.get_attribute("outerHTML")
        soup2=BeautifulSoup(nice,"lxml")
        link=site_name+soup2.find('a')['href']
        print(soup2.text,"\n")
        aniname=soup2.text
        confirm=input("Is it %s:\n"%(aniname))
        if str(confirm)=="yes":
            driver.get(link)
            break
        else:
            pass  
    return site_name
def first_page(ani_url="https://animepahe.com/"):
    global driver
    driver=webdriver.Chrome(options=chrome_options, service=x)
    driver.get(ani_url)
    dezz=driver.find_element(By.NAME, 'q')
    dezz.send_keys(sea)
    #print("OuterHTML:",plan.get_attribute("outerHTML"))
    #print("")
    return link

def daily_anime(ani_url="https://animepahe.com/"):
    soup=BeautifulSoup(driver.page_source,"lxml")
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

def second_page(ulink="https://animepahe.com/anime/1054a99c-7d03-b114-15ae-291da1ee40fc"):
    #driver.implicitly_wait(5)
    #print("\n\n\n",ulink,"-",type(ulink),"\n\n\n")
    driver.get(ulink)
    driver.implicitly_wait(5)
    sleep(2)
    soup=BeautifulSoup(driver.page_source,'lxml')
    dix=soup.find_all("div",class_="episode-number")
    sp=soup.find_all("div",class_="episode-snapshot")
    print(sp)
    driver.implicitly_wait(10)
    eps_num=[]
    for num in dix: 
        ep_num=num.text.replace("Episode","")
        eps_num.append(ep_num.strip())
    print(eps_num)
    driver.implicitly_wait(10)
    for num in eps_num:
        if num==user:
            break
    else:
        print("Number not included")

    new_link="https://animepahe.com"+sp[int(user)-1].a['href']
    driver.get(new_link)
    return new_link

def third_page(ulink="https://animepahe.com/play/1054a99c-7d03-b114-15ae-291da1ee40fc/25930e44622252148dd21525d309fea1e8005c24477e0d1f5dc69461e362c7c5"):
    driver.get(ulink)
    soup=BeautifulSoup(driver.page_source,'lxml')
    dip=soup.find("div", class_='dropdown-menu',id='pickDownload')
    res=dip.find_all("a")
    #print(dip)
    link=''

    for l in res:
        if '720p' in str(l):
            print("Yasss")
            link=l['href']
        else:
            pass
    driver.get(link)
    sleep(7)
    soup=BeautifulSoup(driver.page_source,"lxml")
    pahe=soup.find("div",class_="col-sm-6")
    link2=pahe.a['href']
    driver.get(link2)
    return link2

def last_page(ulink="https://kwik.cx/f/VQyT8njUO1qK"):
    driver.get(ulink)
    soup=BeautifulSoup(driver.page_source,'lxml')
    soup_button=soup.find("button",class_='button is-uppercase is-success is-fullwidth')
    driver.implicitly_wait(30)
    button1=driver.find_element(By.XPATH,'//button[@type="submit"]')
    print(button1.get_attribute('outerHTML'))
    driver.execute_script("arguments[0].click();", button1)

last_page(third_page(second_page(first_page(search()))))

sleep(20)
driver.close()