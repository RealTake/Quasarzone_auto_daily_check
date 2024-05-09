import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

id = sys.argv[1]
pwd = sys.argv[2]

options = Options()

prefs = {"download.default_directory": download_path, 'safebrowsing.enabled': 'True'}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")
options.add_argument("--safebrowsing-disable-download-protection")
options.add_argument("--safebrowsing-disable-extension-blacklist")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

def click_by_js(xpath):
    javaScript = """document.evaluate('{0}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()""".format(xpath)

    driver.execute_script(javaScript)

driver.get("https://quasarzone.com/login")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login_id")))
driver.find_element_by_id("login_id").send_keys(id)
driver.find_element_by_id("password").send_keys(pwd)
driver.find_element_by_id("btn-login").click()
sleep(3)
driver.get("https://quasarzone.com/users/attendance")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "active2")))
driver.find_element_by_css_selector(".active2").click()

driver.close()
driver.quit()