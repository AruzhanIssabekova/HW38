from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application")

driver.get("https://uchet.kz/kursi_valut/")

wait = WebDriverWait(driver, 10)

prices = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//td[text()='₸']/following-sibling::td")))

for price in prices:
    print(price.text)

driver.quit()
