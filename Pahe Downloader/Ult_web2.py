import os
from bs4 import BeautifulSoup
from tkinter.messagebox import askyesno
import inflect
import requests
import threading
from math import floor
from time import sleep
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from API import RestAPI
class Ani_Installer():
    def __init__(self):
        global p,pl, chrome_options, c_options, x, web, list3, list4, list5, site_name
        p=inflect.engine()
        chrome_options = Options()
        c_options = Options()
        chrome_options.add_extension('fdm.crx')
        chrome_options.add_experimental_option("detach", True)
        c_options.add_argument("window-size=1920x1080")
        c_options.add_argument('--headless')
        c_options.add_argument('--disable-gpu')
        x=Service('C:\Program Files (x86)\chromedriver.exe')
        self.web=[]
        self.list4=[]
        self.list5=[]
        self.confirmation=1
        self.sea=str()
        self.resol=str()
        self.name_list=list()
        self.stor=str()
        self.fe=float()
        self.le=float()
        self.restart=bool()
        self.confirm=str()
        pl=RestAPI()
        site_name="https://animepahe.com/"
    def search(self,tkin_root):
        global link, pl,web,list3,list4
        self.driver=webdriver.Chrome(service=x, options=c_options)
        #self.sea=input("What do you want to search: ")
        #self.resol=input("In which resolution: ")
        #self.stor=input("Do you want to know the storage: ")
        #self.fe=int(input("What is the first episode to be downloaded: "))
        #self.le=int(input("What is the last episode to be downloaded: "))
        if self.resol =="720" or self.resol=="720p" or self.resol=="1080" or self.resol=="1080p" or self.resol=="360p" or self.resol=="360":
            pass
        else:
            exit()
        self.driver.get(site_name)
        self.driver.implicitly_wait(10)
        d=self.driver.find_element(By.NAME, 'q')
        d.send_keys(self.sea)
        soup=BeautifulSoup(self.driver.page_source,'lxml')
        search_results=self.driver.find_element(By.CLASS_NAME,'search-results')
        plane= search_results.find_elements(By.TAG_NAME, 'a')
        count=0
        li=["Select anime"]
        for plan in plane:
            nice=plan.get_attribute("outerHTML")
            self.name_list.append(nice)
            soup2=BeautifulSoup(nice,"lxml")
            aniname=soup2.text
            li.append(aniname)
            #self.confirm=input("Is it %s"%(aniname))
        #self.driver.close()
        pl.confirm(list2=li,tkin_root=tkin_root)
        pol=pl.man
        print("ace",pol.get())
        for ani in self.name_list:
            soup2=BeautifulSoup(ani,"lxml")
            link=site_name+soup2.find('a')['href']
            print(soup2.text)
            if pol.get()==soup2.text:
                break
            else:
                pass  
        self.stor=pl.back
        if pl.storage_capacity == True:
            self.confirmation=0
            self.driver.get(site_name)
            dezz=self.driver.find_element(By.NAME, 'q')
            dezz.send_keys(self.sea)
            self.driver.get(link)
            self.download()
            pl.storage_check=askyesno(title="Confirm Capacity", message="The download is %sMB \n Do you wish to continue"%(sum(self.list5)))
            if pl.storage_check==True:
                self.confirmation=1
                self.first_page()
                self.web=[]
                self.list4=[]
                self.list5=[]
                self.download()
                self.driver.close()
            else:
                self.driver.close()
                pl.set_value2()
                self.restart=pl.bac
                print(self.restart)
                pass
    def first_page(self):
        self.driver.close()
        self.driver=webdriver.Chrome(options=chrome_options, service=x)
        self.driver.get(site_name)
        dezz=self.driver.find_element(By.NAME, 'q')
        dezz.send_keys(self.sea)
        self.driver.get(link)
        return link

    def daily_anime(self):
        self.driver=webdriver.Chrome(options=chrome_options, service=x)  
        self.driver.get(site_name)
        soup=BeautifulSoup(self.driver.page_source,"lxml")
        span=soup.find_all("span",class_='episode-title')
        did=soup.find_all("div", class_='episode-number')
        for pi in did:
            if pi.text == "":
                pass
            else:
                print("\n"+pi.text.strip())
        return self.driver
    def search2(self,ulink):
        global soup, dix, sp, eps_num, lm
        wait=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'episode-number')))
        wait2=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'episode-snapshot')))
        soup=BeautifulSoup(self.driver.page_source,'lxml')
        dix=soup.find_all("div",class_="episode-number")
        sp=soup.find_all("div",class_="episode-snapshot")
        self.driver.implicitly_wait(10)
        eps_num=[]
        lm=[]
        self.driver.implicitly_wait(10)
        for num1 in dix:  
            ep_num=num1.text.replace("Episode","")
            if "-" in ep_num:
                head, sep, tail = ep_num.strip().partition('-')
                eps_num.append(float(head))
                for main in range(int(ep_num.strip()[0])+1,int(ep_num.strip()[-1])+1):
                    lm.append(float(main))
                pass
            else:
                eps_num.append(float(ep_num.strip()))
        #print(eps_num)
        #print(lm)

    def download(self):
        for num in range(int(self.fe),int(self.le+1)):
            global link, lm
            i=0
            global new_link
            while i!=1:
                self.search2(link)
                num3=num
                if num in lm:
                    i=1
                    pass
                else:
                    if num not in eps_num:
                        if num>max(eps_num):
                            print(eps_num)
                            nextin=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="page-link next-page"]')))
                            self.driver.implicitly_wait(10)
                            nextin.click()
                            sleep(1)
                            i=0
                        if num<min(eps_num):
                            num+=(min(eps_num)-1)
                    if num<=max(eps_num) and num in eps_num and  num>30:
                            num2=num-(30*(num//30))
                            new_link="https://animepahe.com"+sp[num2-1].a['href']  
                            self.web.append(new_link)
                            i=1
                    elif num<=max(eps_num) and num in eps_num and  num<=30:
                            new_link="https://animepahe.com"+sp[num3-1].a['href']
                            self.web.append(new_link)
                            i=1
                    else:
                        pass
        else:
            for x in self.web:
                self.driver.get(x)
                list3=[]
                self.find_storage(x,list3)
                if self.confirmation==1:
                    self.last_page(self.third_page(x))  
            if self.confirmation==1:
                pl.show_storage(sum(self.list5),"was")
        return self.driver
    def find_storage(self,x,list3):   
        storage=requests.get(x).text
        bread=BeautifulSoup(storage,"lxml")
        dropdown=[]
        dropdow=bread.find_all("a",class_="dropdown-item" )
        for t in dropdow:
            if t.text=="":
                pass
            else:
                dropdown.append(t)
        print(dropdown)
        for l in dropdown:
            if self.resol in str(l) and "eng" not in str(l):
                link=l.text
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
            self.list4.append(stor.strip())
            print(self.list4)
            for mn in self.list4:
                for x in mn:
                    if x.isdigit():
                        pass
                    else:
                        mn=mn.replace(x,"",1)
            self.list5.append(int(mn))
        self.resol = self.resol
        return sum(self.list5)
    def third_page(self,ulink):
        soup=BeautifulSoup(self.driver.page_source,'lxml')
        dip=soup.find("div", class_='dropdown-menu',id='pickDownload')
        res=dip.find_all("a")
        link=''
        
        for l in res:
            if self.resol in str(l):
                link=l['href']
            else:
                pass
        if link=='':
            print("No resolution")
        else:
            pass
        self.driver.get(link)
        wait=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Continue')))
        soup=BeautifulSoup(self.driver.page_source,"lxml")
        pahe=soup.find("div",class_="col-sm-6")
        link2=pahe.a['href']
        return link2
    def downloader(self,x):
        self.search(x)
        if pl.back==False:
            if pl.storage_capacity==False:
                self.first_page()
                self.download()
                self.driver.close()
        else:
            pass
                
    def last_page(self,ulink):
        self.driver.get(ulink)
        button1=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]')))
        self.driver.execute_script("arguments[0].click();", button1)
