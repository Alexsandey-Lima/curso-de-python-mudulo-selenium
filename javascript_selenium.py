import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
service = Service(r"C:\Users\alexs\anaconda3\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

caminho = r'''
https://www.youtube.com/results?search_query=python
'''


driver.get(caminho)


for i in range(30):
    qtd_scroll = i * 2000
    script = f'window.scroll(0,{qtd_scroll})'
    driver.execute_script(script)
    time.sleep(2)
videos = driver.find_elements(By.ID, r'thumbnail')
qtd_videos = 0
for video in videos:
    if video.get_attribute('href') != None:
        print(f"{video.get_attribute('href')}")
        qtd_videos+=1

print(f"encontramos {qtd_videos} videos")
