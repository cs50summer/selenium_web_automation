import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver="C:/Users/akram/chromedriver"
driver=webdriver.Chrome(chrome_driver)

#This test verifies user sign up . However , it goes only until the step where it has to enter data .It cannot retrieve verification code to enter and reverify .

def angel_signup():
    print("hi")
    # Navigate to the staging website
    driver.get("https://staging-invest.angel.com")
    #signup link : //*[@id="__next"]/header/div/div/div[1]/p[2]    //*[@id="__next"]/header/div/div/div[1]/p[2]
    driver.maximize_window()
    sign_up=driver.find_element(By.XPATH,"//*[@id='__next']/header/div/div/div[1]/p[2]")
    sign_up.click()

    driver.implicitly_wait(10)

    #email link: //*[@id="headlessui-dialog-1"]/div/div[2]/div/div/div/div/div/div/form/div/div/input[1]
    email=driver.find_element(By.XPATH,"//*[@id='headlessui-dialog-1']/div/div[2]/div/div/div/div/div/div/form/div/div/input[1]")
    email.send_keys("xyz@xyz.com")

    #passwd link://*[@id="headlessui-dialog-1"]/div/div[2]/div/div/div/div/div/div/form/div/div/input[2]
    passwd=driver.find_element(By.XPATH,"//*[@id='headlessui-dialog-1']/div/div[2]/div/div/div/div/div/div/form/div/div/input[2]")
    passwd.send_keys("Abc123!!")

    driver.implicitly_wait(10)
    #//*[@id="headlessui-dialog-1"]/div/div[2]/div/div/div/div/div/div/form/div/div/input[3]

    #confirn passwd: //*[@id="headlessui-dialog-1"]/div/div[2]/div/div/div/div/div/div/form/div/div/input[2]   //*[@id="headlessui-dialog-42"]/div/div[2]/div/div/div/div/div/div/form/div/div/input[3]
    confirm_passwd=driver.find_element(By.XPATH,"//*[@id='headlessui-dialog-1']/div/div[2]/div/div/div/div/div/div/form/div/div/input[3]")
    confirm_passwd.send_keys("Abc123!!")

    #agree to terms ://*[@id="terms-checkbox"]
    agree_terms=driver.find_element(By.XPATH,"//*[@id='terms-checkbox']")
    agree_terms.click()

    #sign up: //*[@id="headlessui-dialog-7"]/div/div[2]/div/div/div/div/div/div/form/div/div/button
    #//*[@id="headlessui-dialog-1"]/div/div[2]/div/div/div/div/div/div/form/div/div/button/span
    #//*[@id="headlessui-dialog-1"]/div/div[2]/div/div/div/div/div/div/form/div/div/button/span
    #//*[@id="headlessui-dialog-1"]/div/div[2]/div/div/div/div/div/div/form/div/div/button
    btn_signup=driver.find_element(By.XPATH,"//*[@id='headlessui-dialog-1']/div/div[2]/div/div/div/div/div/div/form/div/div/button")
    btn_signup.click()

    #driver.close()

    driver.get("https://www.gmail.com")
    gmail=driver.find_element(By.XPATH,"//*[@id='identifierId']")
    gmail.send_keys("angelfundingtest1@gmail.com")
    next_btn=driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button/div[3]")
    next_btn.click()
    passwd=driver.find_element(By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input")
    passwd.send_keys("Angel_2022")

angel_signup()

#//*[@id="identifierId"]
#//*[@id="m_4410320748229901064templateBody"]/table/tbody/tr/td/table[3]/tbody/tr/td/table/tbody/tr/td/div/div/h1/text()