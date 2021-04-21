import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

download_path = 'D:\\temp\\chrome_download\\'
chrome_path = r"D:\Python\chromedriver2.38.exe"
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_path, 'safebrowsing.enabled': 'True'}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")
options.add_argument("--safebrowsing-disable-download-protection")
options.add_argument("--safebrowsing-disable-extension-blacklist")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path=chrome_path, options=options)

driver.get('https://quasarzone.com/users/attendance')

id = sys.argv[1]
pwd = sys.argv[2]

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login_id"]'))).send_keys(id)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(pwd)
time.sleep(2)
driver.execute_script("document.querySelector('#frm > div > div.top-input-area > p > a').click()")

WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[onclick^=anttendanceCheck]'))).click()

driver.close()