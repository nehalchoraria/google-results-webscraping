import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36')    
browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options) #ChromeDriverManager().install(),

url='https://www.google.com/search?q=hello+world&num=30&gl=JP'

browser.get(url)
soup = BeautifulSoup(browser.page_source,'html.parser') 
items = soup.find_all('div',{'class':'rc'})

print('counts : ' + str(len(items)))
for each in items:
    try:
        print(each.find('div',{'class':'r'}).find('h3').text)
        print(each.find('div',{'class':'s'}).find('span').text)
        print('-------------------------------')
    except:
        pass



