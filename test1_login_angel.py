import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#import time
#from selenium.webdriver.chrome.options import Options


#driver=webdriver.Chrome("C:\\Users\\akram\\chromedriver.exe")
#driver=webdriver.Chrome("C:/Users/akram/chromedriver.exe")
chrome_driver="C:/Users/akram/chromedriver"
driver=webdriver.Chrome(chrome_driver)
def angel_login():
    print("hi")
    #Navigate to the staging website
    driver.get("https://staging-invest.angel.com")
    driver.maximize_window()

    #Click on login button on the top right hand corner of the page
    #By Xpath
    #driver.find_element(By.XPATH,"//*[@id='__next']/header/div/div/div[1]/p[1]").click()

    #By CSS selector
    driver.find_element(By.CSS_SELECTOR, "#__next > header > div > div > div.flex.flex-row.text-black.absolute.hidden.md\:flex.right-10 > p.mr-10.hidden.md\:block.cursor-pointer").click()

    #Enter login and password and click Login

    #User_name=driver.find_element(By.XPATH,"//*[@id='headlessui-dialog-1']/div/div[2]/div/div/div/div/div/div/form/input[1]").click()
    #User_name.sendKeys("xyz")

    User_name=driver.find_element(By.XPATH,"//*[@id='headlessui-dialog-1']/div/div[2]/div/div/div/div/div/div/form/input[1]")
    User_name.send_keys("angelfundingtest1@gmail.com")

    passwd=driver.find_element(By.XPATH,"//*[@id='headlessui-dialog-1']/div/div[2]/div/div/div/div/div/div/form/input[2]")
    passwd.send_keys("Abc123!!")

    login_button=driver.find_element(By.XPATH,"//*[@id='headlessui-dialog-1']/div/div[2]/div/div/div/div/div/div/form/button[1]/span")
    login_button.click()

    driver.close()


angel_login()