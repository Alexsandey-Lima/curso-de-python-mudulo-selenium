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

link='https://pbdatatrader.com.br/jogosdodia'

#service= Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

driver.get(link)
time.sleep(10)

iframe = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe)

iframe = driver.find_element(By.TAG_NAME, 'iframe')

driver.switch_to.frame(iframe)

texto = driver.find_element(By.XPATH, r'/html/body/div[1]/report-embed/div/div[1]/div/div/div/div/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[2]/div/visual-modern/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div[8]').text
print(texto)
