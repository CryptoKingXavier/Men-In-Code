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
but=driver.find_element(By.XPATH, '//div[@class="reload"]')
driver.execute_script("arguments[0].click();", but)
sleep(5)
soup=BeautifulSoup(driver.page_source,"lxml")
img=soup.find("div",class_='embed-responsive embed-responsive-16by9')
#print(img)
pop=img.iframe['src']
def get_file_content_chrome(driver, uri):
  result = driver.execute_async_script("""
    var uri = arguments[0];
    var callback = arguments[1];
    var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'arraybuffer';
    xhr.onload = function(){ callback(toBase64(xhr.response)) };
    xhr.onerror = function(){ callback(xhr.status) };
    xhr.open('GET', uri);
    xhr.send();
    """, uri)
  if type(result) == int :
    raise Exception("Request failed with status %s" % result)
  return base64.b64decode(result)
find=get_file_content_chrome(driver,pop)
#print(find)
deez=open("New.txt","r")
soup=BeautifulSoup(deez,"lxml")
for link in soup:
    print(link.text)
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')] 
urllib.request.install_opener(opener)
#urllib.request.urlretrieve(str(find),"videos/anipics.mp4")