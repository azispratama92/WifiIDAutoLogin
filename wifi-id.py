# Script AutoLogin Wifi ID oleh Azis R. Pratama
# Modifikasi dari script autologin gmail oleh Hongkiat 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = '80615524601'
passwordStr = '11034897135295'
#usernameStr = 'pratama'
#passwordStr = 'rahasia'

browser = webdriver.Chrome()
browser.get(('file:///home/pratama/wifi-ID/landingPage/Desktop%20Welcome%20Page.html'))

# isikan username voucher wifi ID Anda

username = WebDriverWait(browser, 03).until(
    EC.presence_of_element_located((By.ID, 'username_form')))

username.send_keys(usernameStr)

# memberikan sedikit jeda 3 detik

password = WebDriverWait(browser, 03).until(
    EC.presence_of_element_located((By.ID, 'password_form')))

password.send_keys(passwordStr)

signInButton = browser.find_element_by_name('Submit')
signInButton.click()

# Todo List: 
