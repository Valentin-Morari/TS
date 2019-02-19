from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("file:///c:/Users/Fox/Desktop/Y3/SEM2/TS/lab1/Login_v10/website.html")
user_field = driver.find_element_by_name("userid")
pass_field = driver.find_element_by_name("pswrd")
login_button = driver.find_element_by_name("logbtn")
user_field.send_keys("test")
pass_field.send_keys("run")
login_button.click()
wait = WebDriverWait(driver, 10)
try:
	element = wait.until(EC.element_to_be_clickable((By.ID, "secret")))
finally:
	secret = driver.find_element_by_id("secret")
	print "FOUND THE SECRET!!"
