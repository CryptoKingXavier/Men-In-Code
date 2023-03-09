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
        web=[]
        list3=[]
        list4=[]
        list5=[]
        self.sea=str()
        self.resol=str()
        self.name_list=list()
        self.stor=str()
        self.fe=int()
        self.le=int()
        self.confirm=str()
        pl=RestAPI()
        site_name="https://animepahe.com/"
    def search(self,tkin_root):
        global link, pl
        self.driver=webdriver.Chrome(service=x, options=c_options)
        #self.sea=input("What do you want to search: ")
        #self.resol=input("In which resolution: ")
        #self.stor=input("Do you want to know the storage: ")
        if self.resol =="720" or self.resol=="720p" or self.resol=="1080" or self.resol=="1080p" or self.resol=="360p" or self.resol=="360":
            pass
        else:
            exit()
        #self.fe=int(input("What is the first episode to be downloaded: "))
        #self.le=int(input("What is the last episode to be downloaded: "))
        self.driver.get(site_name)
        self.driver.implicitly_wait(10)
        d=self.driver.find_element(By.NAME, 'q')
        d.send_keys(self.sea)
        soup=BeautifulSoup(self.driver.page_source,'lxml')
        search_results=self.driver.find_element(By.CLASS_NAME,'search-results')
        plane= search_results.find_elements(By.TAG_NAME, 'a')
        count=0
        li=[]
        for plan in plane:
            nice=plan.get_attribute("outerHTML")
            self.name_list.append(nice)
            soup2=BeautifulSoup(nice,"lxml")
            aniname=soup2.text
            li.append(aniname)
            #self.confirm=input("Is it %s"%(aniname))
        self.driver.close()
        pl.confirm(list2=li,tkin_root=tkin_root)
        pol=pl.man
        print(pol.get())
        for ani in self.name_list:
            soup2=BeautifulSoup(ani,"lxml")
            link=site_name+soup2.find('a')['href']
            print(soup2.text)
            if pol.get()==soup2.text:
                break
            else:
                pass  
    def first_page(self):
        self.driver=webdriver.Chrome(options=chrome_options, service=x)
        self.driver.get(site_name)
        dezz=self.driver.find_element(By.NAME, 'q')
        dezz.send_keys(self.sea)
        self.driver.get(link)
        if self.stor == True:
            self.search2(link)
            for y in web:
                list3=[]
                self.find_storage(x=y,list3=list3)
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
        global soup, dix, sp, eps_num, nextin
        wait=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'episode-number')))
        wait2=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'episode-snapshot')))
        soup=BeautifulSoup(self.driver.page_source,'lxml')
        dix=soup.find_all("div",class_="episode-number")
        sp=soup.find_all("div",class_="episode-snapshot")
        self.driver.implicitly_wait(10)
        nextin=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="page-link next-page"]')))
        eps_num=[]
        self.driver.implicitly_wait(10)
        for num1 in dix:  
            ep_num=num1.text.replace("Episode","")
            eps_num.append(ep_num.strip())

    def download(self):
        for num in range(self.fe,(self.le+1)):
            i=0
            global new_link, link
            while i!=1:
                self.search2(link)
                if num<=int(eps_num[-1]) and str(num) in eps_num and  num>30:
                        num2=num-(30*(num//30))
                        new_link="https://animepahe.com"+sp[num2-1].a['href']  
                        web.append(new_link)
                        i=1
                elif num<=int(eps_num[-1]) and str(num) in eps_num and  num<=30:
                        new_link="https://animepahe.com"+sp[num-1].a['href']
                        web.append(new_link)
                        i=1
                else:
                    nextin.click()
                    sleep(1)
                    i=0
            
        else:
            for x in web:
                self.driver.get(x)
                list3=[]
                self.find_storage(x,list3)
                self.last_page(self.third_page(x))
            #print(list5)
            pl.show_storage(sum(list5),"was")
        return self.driver
    def find_storage(self,x,list3):   
        storage=requests.get(x).text
        bread=BeautifulSoup(storage,"lxml")
        dropdown=bread.find_all("div",id="pickDownload" )
        print(dropdown)
        for l in dropdown:
            if self.resol in str(l):
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
        self.resol = self.resol
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
            self.first_page()
            self.download()
            self.driver.close()
        else:
            pass
    def last_page(self,ulink):
        self.driver.get(ulink)
        button1=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]')))
        self.driver.execute_script("arguments[0].click();", button1)
