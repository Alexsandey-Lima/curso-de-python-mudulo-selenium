import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
service = Service(r"C:\Users\alexs\anaconda3\chromedriver.exe")
#driver = webdriver.Chrome(service=service)

caminho = r'''
https://www.hashtagtreinamentos.com/
'''


#service= Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

#driver.get(caminho)
#driver.maximize_window()
#driver.minimize_window()

#para ele nem abrir
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver2 = webdriver.Chrome(service=service, options=options)

driver2.get(caminho)


itens = driver2.find_elements(By.CLASS_NAME, r'texto-topo-home')

for item in itens:
    print(item.text)