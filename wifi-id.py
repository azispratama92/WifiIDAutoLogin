# Script AutoLogin Wifi ID oleh Azis R. Pratama
# Modifikasi dari script auto-login gmail oleh Hongkiat (https://github.com/hongkiat/autologinbot) 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# isikan username (baris 9) & password (baris 10) voucher wifi ID Anda di dalam tanda '...' berikut:
usernameStr = '80615581892'
passwordStr = '11034727408335'

browser = webdriver.Chrome()
# Ganti alamat URL wifi ID landing page, sesuai dengan alamat mac Anda: 
browser.get(('http://welcome2.wifi.id/wifi.id-new/default/?gw_id=WAG-D4-KBU&client_mac=08:3e:8e:27:0a:9d&wlan=SMNSMN00053/TLK-WI329744-0002:@wifi.id&sessionid=0A00FFFF7802E0A7-5997AC79&redirect=http://wifi.id/'))

# baris nomor 16 ke bawah berikut tidak perlu dimodifikasi (biarkan apa adanya): 

username = WebDriverWait(browser, 01).until(
    EC.presence_of_element_located((By.ID, 'username_form')))

username.send_keys(usernameStr)

# memberikan sedikit jeda selama 3 detik

password = WebDriverWait(browser, 01).until(
    EC.presence_of_element_located((By.ID, 'password_form')))

password.send_keys(passwordStr)

signInButton = browser.find_element_by_name('Submit')
signInButton.click()
