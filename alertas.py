import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

service = Service(r"C:\Users\alexs\anaconda3\chromedriver.exe")
driver = webdriver.Chrome(service=service)

caminho = r'''
C:\Users\alexs\PycharmProjects\AULAS PYTHON IMPRESSIONADOR\SELENIUM\alertas.html
'''


#service= Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

driver.get(caminho)

driver.find_element(By.XPATH, r'/html/body/div[1]/input').click()

#alerta = driver.switch_to.alert

alerta = Alert(driver)
alerta.accept()
driver.find_element(By.XPATH, r'/html/body/div[2]/input').click()
alerta = Alert(driver)
text = alerta.text
print(text)
#aceitar
alerta.accept()
#cancelar
#alerta.dismiss()
time.sleep(3)
driver.find_element(By.XPATH, r'/html/body/div[3]/button').click()
alerta = Alert(driver)
alerta.send_keys('111.111.111-11')
alerta.accept()


time.sleep(20000)

