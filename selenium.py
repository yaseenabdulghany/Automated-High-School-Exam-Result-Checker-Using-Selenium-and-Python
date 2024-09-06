def searchInternet():
    search = input("What do you want to look up?: ")
    chrome_driver = webdriver.Chrome()
    def test_lambdatest_google():
        chrome_driver.get('https://www.google.com')
        chrome_driver.maximize_window()
        if not "Google" in chrome_driver.title:
            raise Exception("Could not load page")
        element = chrome_driver.find_element_by_name("q")
        element.send_keys(search)
        element.submit()

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

seat_number = input()
driver : webdriver = webdriver.Chrome()
driver.get('https://g12.emis.gov.eg/')

wr :WebElement=driver.find_element(by=By.XPATH,value='//*[@id="SeatingNo"]')
wr.send_keys(f'{seat_number}')

z : WebElement=driver.find_element(by=By.XPATH,value='//*[@id="featured-services mt-5"]/div/div/div/div[1]/div/form/button')
z.click()

searchInternet()

