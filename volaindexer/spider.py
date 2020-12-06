import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
chrome_path = r"/usr/bin/chromedriver"
PROXY = "186.22.162.178:8080" # IP:PORT or HOST:PORT
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('headless')
options.add_argument('--no-sandbox')
options.add_argument("--incognito")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--proxy-server=http://%s' % PROXY)
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(3)
driver.get("https://volafile.org/r/pytq6a7r")
#if driver.find_element_by_link_text('front page').exists():
    #print("existe")
#passw = driver.find_elements_by_name('password')
#passw[0].send_keys("12345")
#print(passw)
print(driver.page_source)




#print(botao)
#botao[1].click()
#time.sleep(3)
#passw = driver.find_elements_by_name('password')
#print(passw)
driver.close()
