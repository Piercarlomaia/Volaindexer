import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Users\NASA\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
driver.get('https://volafile.org/r/efy908bw')
html = driver.page_source
soup = BeautifulSoup(html)

soup = str(soup)
file = open('testfile.txt','w')

file.write(soup)


file.close()
