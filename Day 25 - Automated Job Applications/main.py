from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_WEBDRIVER = "/Users/danielkrsak/PycharmProjects/chromedriver"
EMAIl = "daniel.krsak@bolt.eu"
PASSWORD = "Lamerisko123!"

driver = webdriver.Chrome(CHROME_WEBDRIVER)
driver.get("https://www.linkedin.com/home")

driver.find_element(By.LINK_TEXT,"Sign in").click()
driver.find_element(By.NAME, "session_key").send_keys(EMAIl)
driver.find_element(By.NAME, "session_password").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#global-nav-typeahead input").send_keys("Python Developer")
driver.find_element(By.CSS_SELECTOR, "#global-nav-typeahead input").send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[3]/button').click()
time.sleep(5)
job_list = driver.find_elements(By.CLASS_NAME, "job-card-list__title")
driver.find_element(By.LINK_TEXT, job_list[0].text).click()
driver.find_element(By.CSS_SELECTOR, ".mt5 .jobs-save-button").click()




