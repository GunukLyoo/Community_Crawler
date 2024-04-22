from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def Crawling(driver, id):
    url = 'https://twitter.com/' + id
    
    driver.get(url)
    time.sleep(4)

    name = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]//div[@data-testid="tweetText"]')
    
    return name.text