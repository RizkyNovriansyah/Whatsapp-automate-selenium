from selenium import webdriver
import csv
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

name = input('enter name : ')
msg = input('msg : ')
count = int(1)

input('enter anything after logged in')

with open("data.csv") as files:
    datas = csv.reader(files)
    user = None
    button = None
    
    search_column = driver.find_element_by_class_name('_3FRCZ')
    for data in datas:
        print(data[1])
        search_column.send_keys(data[1])
        time.sleep(1)
        name = data[1]
        username = data[2]
        password = data[3]
        
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)) 
        while user is None :
            pass
        user.click()
        time.sleep(1)
        driver.find_element_by_class_name('_3uMse').click()

        time.sleep(1)
        
        msg = "Welcome!"
        ActionChains(driver).send_keys(msg).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()

        msg = "Name : *"+username+"*"
        ActionChains(driver).send_keys(msg).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()

        msg = "Code : *"+password+"*"
        ActionChains(driver).send_keys(msg).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()

        msg = "Please take responsibility for what you do"
        ActionChains(driver).send_keys(msg).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()

        msg = "-"+str(name)
        ActionChains(driver).send_keys(msg).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()

        #msg_box.send_keys(msg)
        time.sleep(1)
        button = driver.find_element_by_class_name('_1U1xa')
        time.sleep(1)
        button.click()
        time.sleep(1)
