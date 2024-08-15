import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager

service = Service(r"C:\Users\alexs\anaconda3\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# service= Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

caminho = r'''
https://www.hashtagtreinamentos.com/
'''
driver.get(caminho)

itens = driver.find_elements(By.XPATH, r'/html/body/div/div[1]/div/div/div[1]/a[1]')

for item in itens:
    if 'cursos hashtag treinamentos' in item.text.lower():
        item.click()
        container = driver.find_elements(By.CLASS_NAME, r'wp-block-image')
        try:
           for item2 in container:
            figure = item2.find_element(By.TAG_NAME, 'figure')
            a = figure.find_element(By.TAG_NAME, 'a')
            print(a.get_attribute('href'))
            # print(item.get_attribute('href'))

        except:
            pass
    break


