from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver_path = "/Users/danielkrsak/PycharmProjects/chromedriver"
driver = webdriver.Chrome(chromedriver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
upgrades = driver.find_elements(By.CSS_SELECTOR, "#store b")
upgrades.pop(len(upgrades)-1)

upgrade_dict = {}
upgrade_names = [item.text.split("-")[0].strip() for item in upgrades]

for i in range(len(upgrades)):
    upgrade_dict[i] = {
        upgrades[i].text.split("-")[0].strip().replace(",", ""): upgrades[i].text.split("-")[1].strip().replace(",", "")
    }

time_out = time.time() + 5
five_min = time.time() + 60*5
time.sleep(2)

while True:
    cookie.click()
    if time.time() > time_out:
        total_biscuits = driver.find_element(By.ID, "money").text
        for i in range(len(upgrade_names)-1, -1, -1):
            if total_biscuits >= upgrade_dict[i][upgrade_names[i]]:
                available_upgrade = driver.find_element(By.ID, "buy" + f"{upgrade_names[i]}")
                available_upgrade.click()
                timeout = time.time() + 5
                break
            else:
                continue
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

