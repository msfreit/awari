from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randrange

# ABRO O CHROME
driver = webdriver.Chrome(ChromeDriverManager().install())
# abro o whatsapp
driver.get('https://twitter.com/login')
sleep(1)

# campo email
xpath = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
# clico nele
xpath.click()

xpath.send_keys('mauricio.freitas@hotmail.com')

#senha
xpath = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
xpath.click()
xpath.send_keys('@119a9af0')

# clica em login
xpath = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
xpath.click()
