import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from PIL import Image

service = Service(r"C:\Users\alexs\anaconda3\chromedriver.exe")
driver = webdriver.Chrome(service=service)

caminho = r'''
https://www.hashtagtreinamentos.com/cursos-hashtag-treinamentos'''


#service= Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

driver.get(caminho)

imagem_completa = driver.save_screenshot('print.png')
elemento = driver.find_element(By.XPATH, r'/html/body/header')
posicao = elemento.location
tamanho = elemento.size
x_inicial = posicao['x']*1.25
x_final = x_inicial + tamanho['width']
y_inicial = posicao['y']*1.25
y_final = y_inicial + tamanho['height']
imagem = Image.open('print.png')
image = imagem.crop((x_inicial,y_inicial,x_final,y_final))
image.save('print_pedaço.png')

