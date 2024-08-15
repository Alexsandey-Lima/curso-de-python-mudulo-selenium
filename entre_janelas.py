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
https://www.hashtagtreinamentos.com/cursos-hashtag-treinamentos'''


#service= Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

driver.get(caminho)

driver.find_element(By.XPATH, r'/html/body/section[2]/div/div[6]/figure/a/picture/img').click()
aba_original = driver.window_handles[0]
nova_aba = driver.window_handles[1]

driver.switch_to.window(nova_aba)
driver.find_element(By.XPATH, r'/html/body/div/div[2]/div/div[2]/form/div[1]/input').send_keys('Alex')

#fecha 1 aba
#driver.close()

#fecha o navegador
#driver.quit()
time.sleep(20000)