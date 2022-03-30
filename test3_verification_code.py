import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#pip install --upgrade pip
#pip install undetected_chromedriver
import undetected_chromedriver.v2 as uc


chrome_driver="C:/Users/akram/chromedriver"
#driver=webdriver.Chrome(chrome_driver)
#driver=uc.Chrome()

if __name__=='__main__':

        #def verification_code():
        #driver.get("https://www.gmail.com")
        driver = uc.Chrome()





        driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        driver.maximize_window()
        gmail = driver.find_element(By.XPATH, "//*[@id='identifierId']")
        gmail.send_keys("angelfundingtest1")
        sleep(3)
        #// *[ @ id = "identifierNext"] / div / button / span
        #// *[ @ id = "identifierNext"] / div / button / span
        #//*[@id="next"]/div/button/span

        #try_again_button=driver.find_element(By.XPATH,"//*[@id='next']/div/button/span").click()
        ##next > div > button > span
       #//*[@id="password"]/div[1]/div/div[1]/input
        #//*[@id="identifierNext"]/div/button/span

        next_btn = driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span")
        next_btn.click()
        sleep(5)

        #try_again_button = driver.find_element(By.CSS_SELECTOR, "#next > div > button > span")
        #try_again_button.click()
        #gmail.send_keys("angelfundingtest1@gmail.com")
        #next_btn = driver.find_element(By.XPATH, " // *[ @ id = 'identifierNext'] / div / button/ span")
        #next_btn.click()

        passwd = driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")
        passwd.send_keys("Angel_2022")
        sleep(3)

        next_btn=driver.find_element(By.XPATH,"//*[@id='passwordNext']/div/button/span").click()
        sleep(8)
       # email_list=driver.find_element(By.XPATH,"/html/body/iframe[1]").click()
        #sleep(4)

        driver.find_element(By.XPATH,"// *[ @ id = ':1'] / div / div / div[7]") .click()
        sleep(4)



    #verification_code()