from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class Crawler:
    #트위터 최상단의 트윗을 크롤링 해오는 함수
    #def TwitterCrawling(driver: webdriver, id: str) -> str:
    def TwitterCrawling(driver: webdriver, id: str):
        url = 'https://twitter.com/' + id
    
        driver.get(url)
        time.sleep(4)
        #print(Crawler.twit_check(driver))

        name = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]//div[@data-testid="tweetText"]')
        
        #test = driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(3) > div > div > section > div > div > div:nth-child(1) > div')
        #test = driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(3) > div > div > section > div > div > div:nth-child(1) > div > div > article > div > div > div > div > div:nth-child(2)')
        test_list = driver.find_elements(By.CSS_SELECTOR, '#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(3) > div > div > section > div > div > div:nth-child(n) > div')
        print(len(test_list))
        for test in test_list:
            print(Crawler.twit_check(test))
            print(test.find_element(By.CSS_SELECTOR, 'div > article > div > div > div > div > div > div[data-testid="tweetText]').text)
            #div > article > div > div > div > div > div:nth-child(2) > div[data-testid="tweetText] 
            
        
        #print(test.text)
    
       # return name.text

    #해당 트윗이 메인으로 설정된 트윗인지 아니면 재게시된 트윗인지 확인하는 함수
    def twit_check(driver: webdriver):
        try:
            #c = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]//div[@data-testid="socialContext"]')
            #c = driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(3) > div > div > section > div > div > div:nth-child(1) > div > div > article > div > div > div:nth-child(1) > div > div > div > div > div > div > div > div[data-testid = "socialContext"]')
            c = driver.find_element(By.CSS_SELECTOR, 'div > article > div > div > div:nth-child(1) > div > div > div > div > div > div > div > div[data-testid="socialContext"]')
            return c.text
        except NoSuchElementException as e:
            return "None"
