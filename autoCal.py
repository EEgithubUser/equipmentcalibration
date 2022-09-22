from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

file = 'config.ini'
config = ConfigParser()
config.read(file)

s = Service(config['service']['address'])
driver = webdriver.Chrome(service = s)
driver.get("https://www.pmi-link.com/login.php")

driver.find_element(By.CSS_SELECTOR,"input[id='user']").send_keys(config['account']['username'])
driver.find_element(By.CSS_SELECTOR,"input[id='pass']").send_keys(config['account']['password'])
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
driver.find_element(By.XPATH,"(//a[@class='dropdown-toggle'])[2]").click()
driver.find_element(By.XPATH,"(//a[@title='Create Shipper'])[1]").click()
driver.find_element(By.XPATH,"(//input[@class='field'])[3]").click()
wait = WebDriverWait(driver,20)
time.sleep(10)
wait.until(EC.element_to_be_clickable((By.XPATH,"(//img[@alt='next day pickup'])"))).click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
driver.find_element(By.CSS_SELECTOR,"select[id='shipTo']").click()
driver.find_element(By.CSS_SELECTOR,"option[value='2']").click()
driver.find_element(By.CSS_SELECTOR,"input[id='contact']").click()
driver.find_element(By.CSS_SELECTOR,"input[id='contact']").send_keys(config['info']['contact'])
driver.find_element(By.CSS_SELECTOR,"input[id='phone']").click()
driver.find_element(By.CSS_SELECTOR,"input[id='phone']").send_keys(config['info']['phone'])
driver.find_element(By.CSS_SELECTOR,"input[id='email']").click()
driver.find_element(By.CSS_SELECTOR,"input[id='email']").send_keys(config['info']['email'])
driver.find_element(By.CSS_SELECTOR,"input[id='city']").click()
driver.find_element(By.CSS_SELECTOR,"input[id='city']").clear()
driver.find_element(By.CSS_SELECTOR,"input[id='city']").send_keys(config['info']['city'])
driver.find_element(By.CSS_SELECTOR,"select[name='Location']").click()
driver.find_element(By.CSS_SELECTOR,"option[value='Other']").click()
driver.find_element(By.CSS_SELECTOR,"input[name='Comments']").click()
driver.find_element(By.CSS_SELECTOR,"input[name='Comments']").send_keys(config['info']['location'])