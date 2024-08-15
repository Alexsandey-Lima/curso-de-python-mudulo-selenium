import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


service = Service(r"C:\Users\alexs\anaconda3\chromedriver.exe")
driver = webdriver.Chrome(service=service)

caminho = r'''
https://www.hashtagtreinamentos.com/
'''


#service= Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

driver.get(caminho)

menu = driver.find_element(By.XPATH, r'/html/body/header/nav/ul/li[4]')
item = driver.find_element(By.XPATH, r'/html/body/header/nav/ul/li[4]/ul/li[4]/a')
#link = elemento.get_attribute('href')
#driver.get(link)

ActionChains(driver).move_to_element(menu).perform()
item.click()

time.sleep(20000)