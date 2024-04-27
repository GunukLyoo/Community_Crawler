from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class Crawler:
    #트위터 최상단의 트윗을 크롤링 해오는 함수
    def TwitterCrawling(driver, id):
        url = 'https://twitter.com/' + id
    
        driver.get(url)
        time.sleep(4)
        print(Crawler.twit_check(driver))

        name = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]//div[@data-testid="tweetText"]')
    
        return name.text

    #해당 트윗이 메인으로 설정된 트윗인지 아니면 재게시된 트윗인지 확인하는 함수
    def twit_check(driver):
        try:
            c = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]//div[@data-testid="socialContext"]')
            return c.text
        except NoSuchElementException as e:
            return "None"
        