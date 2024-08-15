import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
service = Service(r"C:\Users\alexs\anaconda3\chromedriver.exe")
driver = webdriver.Chrome(service=service)

caminho = r'''
https://www.hashtagtreinamentos.com/
'''


#service= Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

driver.get(caminho)


#while len(driver.find_elements(By.CLASS_NAME,r"eicon-close")) <1:
 #   time.sleep(1)

#time.sleep(1)
#driver.find_element(By.CLASS_NAME,r"eicon-close").click()

elemento = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME,r"eicon-close")))

driver.find_element(By.CLASS_NAME,r"eicon-close").click()
