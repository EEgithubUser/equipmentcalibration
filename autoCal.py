from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


webpage = "https://www.pmi-link.com/login.php"


class SendCalibrationRequest():

	def config_setup(self):
		file = 'config.ini'
		self.config = ConfigParser()
		self.config.read(file)

	def webpage_setup(self):
		s = Service(self.config['service']['address'])
		self.driver = webdriver.Chrome(service = s)
		self.driver.get(webpage)

	def user_login(self):
		self.driver.find_element(By.CSS_SELECTOR,"input[id='user']").send_keys(self.config['account']['username'])
		self.driver.find_element(By.CSS_SELECTOR,"input[id='pass']").send_keys(self.config['account']['password'])
		self.driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()

	def create_shipper(self):
		self.driver.find_element(By.XPATH,"(//a[@class='dropdown-toggle'])[2]").click()
		self.driver.find_element(By.XPATH,"(//a[@title='Create Shipper'])[1]").click()
		self.driver.find_element(By.XPATH,"(//input[@class='field'])[3]").click()

	def user_input_pause(self):
		wait = WebDriverWait(self.driver,20)
		time.sleep(10)
		wait.until(EC.element_to_be_clickable((By.XPATH,"(//img[@alt='next day pickup'])"))).click()

	def tab1_switch(self):
		windowsOpened = self.driver.window_handles
		self.driver.switch_to.window(windowsOpened[1])

	def populate_pickup_request(self):
		self.driver.find_element(By.CSS_SELECTOR,"select[id='shipTo']").click()
		self.driver.find_element(By.CSS_SELECTOR,"option[value='2']").click()
		self.driver.find_element(By.CSS_SELECTOR,"input[id='contact']").click()
		self.driver.find_element(By.CSS_SELECTOR,"input[id='contact']").send_keys(self.config['info']['contact'])
		self.driver.find_element(By.CSS_SELECTOR,"input[id='phone']").click()
		self.driver.find_element(By.CSS_SELECTOR,"input[id='phone']").send_keys(self.config['info']['phone'])
		self.driver.find_element(By.CSS_SELECTOR,"input[id='email']").click()
		self.driver.find_element(By.CSS_SELECTOR,"input[id='email']").send_keys(self.config['info']['email'])
		self.driver.find_element(By.CSS_SELECTOR,"input[id='city']").click()
		self.driver.find_element(By.CSS_SELECTOR,"input[id='city']").clear()
		self.driver.find_element(By.CSS_SELECTOR,"input[id='city']").send_keys(self.config['info']['city'])
		self.driver.find_element(By.CSS_SELECTOR,"select[name='Location']").click()
		self.driver.find_element(By.CSS_SELECTOR,"option[value='Other']").click()
		self.driver.find_element(By.CSS_SELECTOR,"input[name='Comments']").click()
		self.driver.find_element(By.CSS_SELECTOR,"input[name='Comments']").send_keys(self.config['info']['location'])
