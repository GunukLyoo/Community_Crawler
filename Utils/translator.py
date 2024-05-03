from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#텍스트를 파파고 언어 자동인식으로 한글로 번역하여 출력하는 함수
def PaPagoTranslate(driver: webdriver, text: str):
    url = 'https://papago.naver.com/?sk=auto&tk=ko'
    driver.get(url)
    time.sleep(3)

    textbox = driver.find_element(By.ID, 'txtSource')
    textbox.send_keys(text)

    time.sleep(3)

    resultbox = driver.find_element(By.ID, 'txtTarget')
    print(resultbox.text)

#텍스트를 구글 언어 자동인식으로 한글로 번역하여 출력하는 함수
def GoogleTranslate(driver: webdriver, text: str):
    url = 'https://translate.google.co.kr/?hl=ko&sl=auto&tl=ko&op=translate'
    driver.get(url)
    time.sleep(3)
    
    textbox = driver.find_element(By.CLASS_NAME, 'er8xn')
    textbox.send_keys(text)
    
    time.sleep(3)
    
    resultbox = driver.find_element(By.CLASS_NAME, 'ryNqvb')
    print(resultbox.text)
