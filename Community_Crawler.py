from selenium import webdriver
from Crawler.Crawler import Crawler
from Utils.translator import PaPagoTranslate, GoogleTranslate
import time

#트위터 사용자 페이지의 첫번째 트윗을 크롤링하여 자동으로 번역하는 프로그램이다.

print("가져오고자 하는 사람의 계정 id를 입력하시오: ", end='')
id = input()
print("사용하고자 하는 번역기를 입력하시오(파파고: 1, 구글: 2): ", end='')
tl = input()

#url = 'https://twitter.com/suisei_hosimati'

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)

te = Crawler.TwitterCrawling(driver, id)
print(te)

if tl == '1':
    PaPagoTranslate(driver, te)
elif tl == '2':
    GoogleTranslate(driver, te)

driver.quit()
