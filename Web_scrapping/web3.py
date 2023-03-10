from dataclasses import replace
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import snoop
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
x=Service("C:\Program Files (x86)\chromedriver.exe")
fe=70#int(input("First Episode to be downloaded: "))
le=72#int(input("Last Episode to be downloaded: "))
web=[]
list4=[]
list5=[]
pop="720"#input("Resolution: ")
stor="yes"#input("Do you want to know the storage: ")
#@snoop
def driver_find(ulink):
     global driver
     driver=webdriver.Chrome(options=chrome_options, service=x)
     driver.get(ulink)
def search2(ulink="https://animepahe.com//anime/75f4d33d-1a9a-728f-82e9-8d1bb35f37d0"):
    global soup, dix, sp, eps_num, nextin
    soup=BeautifulSoup(driver.page_source,'lxml')
    dix=soup.find_all("div",class_="episode-number")
    sp=soup.find_all("div",class_="episode-snapshot")
    driver.implicitly_wait(10)
    #sleep(2)
    #print(dix)
    driver.implicitly_wait(10)
    if dix==[]:
        sleep(2)
        soup=BeautifulSoup(driver.page_source,'lxml')
        dix=soup.find_all("div",class_="episode-number")
        sp=soup.find_all("div",class_="episode-snapshot")
    #    print(dix)
    driver.implicitly_wait(10)
    #print(dix)
    sleep(2)
    nextin=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="page-link next-page"]')))
    eps_num=[]
    #print(eps_num)
    driver.implicitly_wait(10)
    #while num>30:
    for num1 in dix:  
        ep_num=num1.text.replace("Episode","")
        eps_num.append(ep_num.strip())

def second_page(link):
    driver_find(link)
    for num in range(fe,le+1):
        i=0
        global new_link
        while i!=1:
            search2()
            #new_link=''
            print(eps_num)
            print(num)
            #print("\n"+driver.current_url()+"\n")
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
                sleep(2)
                    #second_page()
        
    else:
        for x in web:
            global stor
            driver.get(x)
            list3=[]
            if stor == "yes":   
                storage=requests.get(x).text
                bread=BeautifulSoup(storage,"lxml")
                dropdown=bread.find_all("div",id="pickDownload" )
                #print(dropdown)
                for l in dropdown:
                    if pop in str(l):
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
    print(list5)
    print("The total storage is",sum(list5),"MB")



                        
#return new_link
second_page("https://animepahe.com//anime/75f4d33d-1a9a-728f-82e9-8d1bb35f37d0")
print("Passed")
sleep(10)
#driver.close()

