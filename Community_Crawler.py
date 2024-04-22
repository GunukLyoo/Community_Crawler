from selenium import webdriver
from Crawler.twitterCrawler import Crawling
from Utils.translator import PaPagoTranslate
import time

#트위터 사용자 페이지의 첫번째 트윗을 크롤링하여 자동으로 번역하는 프로그램이다.

print("가져오고자 하는 사람의 계정 id를 입력하시오: ", end='')
id = input()

#url = 'https://twitter.com/suisei_hosimati'

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)

te = Crawling(driver, id)
print(te)

PaPagoTranslate(driver, te)

driver.quit()