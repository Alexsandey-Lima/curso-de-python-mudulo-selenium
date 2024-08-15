import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
service = Service(r"C:\Users\alexs\anaconda3\chromedriver.exe")
driver = webdriver.Chrome(service=service )

caminho = r'''
C:\Users\alexs\PycharmProjects\AULAS PYTHON IMPRESSIONADOR\SELENIUM\formulario.html
'''
#service= Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

driver.get(caminho)

driver.find_element(By.XPATH, '/html/body/form/input[1]').click()
#alerta
#switch_to troca a janela
alert = driver.switch_to.alert
alert.accept()

#check box
driver.find_element(By.XPATH,'/html/body/form/input[3]').click()
#print(driver.find_element(By.XPATH,'/html/body/form/input[3]').is_selected())

#campo de cor
#print(driver.find_element(By.XPATH, '/html/body/form/input[4]').get_attribute('value'))
driver.find_element(By.XPATH, '/html/body/form/input[4]').send_keys('#834d8d')
driver.find_element(By.XPATH, '/html/body/form/input[5]').send_keys('#2143E8')

#data
driver.find_element(By.XPATH, '/html/body/form/input[6]').send_keys('19/06/2002')
#print(driver.find_element(By.XPATH, '/html/body/form/input[6]').get_attribute("value"))
driver.find_element(By.XPATH, '/html/body/form/input[7]').send_keys('25/05/2023',Keys.TAB,'14:26')

#SELECIONAR ARQUIVO
driver.find_element(By.XPATH, '/html/body/form/input[8]').send_keys(r"C:\Users\alexs\Downloads\Python Impressionador - Alexsandey - Ingles.pdf")


#outras datas
driver.find_element(By.XPATH, '/html/body/form/input[9]').send_keys('junho',Keys.TAB,'2024')

#so numericos
driver.find_element(By.XPATH, '/html/body/form/input[10]').send_keys('2024')

#senha
driver.find_element(By.XPATH, '/html/body/form/input[11]').send_keys('2024')

#radio button
driver.find_element(By.XPATH, '/html/body/form/input[13]').click()

#campo de texto
driver.find_element(By.XPATH, '/html/body/form/input[16]').send_keys('Flamengo')
#print(driver.find_element(By.XPATH, '/html/body/form/input[16]').get_attribute('value'))

#horas
driver.find_element(By.XPATH, '/html/body/form/input[17]').send_keys('17:40')
driver.find_element(By.XPATH, '/html/body/form/input[18]').send_keys('14','2023')

#CLEAR
driver.find_element(By.XPATH, '/html/body/form/textarea').send_keys('Flamengo \nvasco \ncorintians \nchapecoense \nconfiança')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/form/textarea').clear()

#slider
elemento = driver.find_element(By.XPATH, '/html/body/form/input[15]')
elemento.clear()
for i in range(50-30):
    elemento.send_keys((Keys.ARROW_RIGHT))

#preenchendo o valor
elemento = driver.find_element(By.XPATH,'/html/body/form/select[1]').send_keys("C")

elemento = driver.find_element(By.XPATH,'/html/body/form/select[1]/option[2]').click()

elemento = driver.find_element(By.TAG_NAME, 'select')
elemento_select = Select(elemento)
elemento_select.select_by_visible_text("A")
time.sleep(10)
