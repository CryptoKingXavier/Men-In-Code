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
chrome_options.add_extension('fdm.crx')
x=Service("C:\Program Files (x86)\chromedriver.exe")

driver=webdriver.Chrome(options=chrome_options, service=x)
soup=BeautifulSoup(driver.page_source,'lxml')

def last_page(ulink="https://kwik.cx/f/VQyT8njUO1qK"):
    driver.get(ulink)
    soup_button=soup.find("button",class_='button is-uppercase is-success is-fullwidth')
    driver.implicitly_wait(30)
    button1=driver.find_element(By.XPATH,'//button[@type="submit"]')
    print(button1.get_attribute('outerHTML'))
    driver.execute_script("arguments[0].click();", button1)


sleep(20)
driver.close()