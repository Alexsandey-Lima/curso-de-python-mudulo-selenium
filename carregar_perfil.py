import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\alexs\AppData\Local\Google\Chrome\User Data\Profile selenium')

service = Service(r"C:\Users\alexs\anaconda3\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

caminho = r'''
https://web.whatsapp.com/
'''
driver.get(caminho)
time.sleep(120)

