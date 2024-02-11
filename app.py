from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv


driver = webdriver.Chrome()
driver.get("https://sosenskoe-omsu.ru/")

# Поиск выпадающего меню "сферы" и щелчок по нему
menu_dropdown = driver.find_element(By.XPATH,"*//nav[@class='top_menu']/ul/li[5]/a")
menu_dropdown.click()

# Поиск меню "10 лет ТИНАО" и щелчок по нему
docs = driver.find_element(By.XPATH,"*//nav[@class='top_menu']/ul/li[5]/ul/li/a")
docs.click()

# Поиск всех результатов на странице
results = driver.find_elements(By.XPATH,"//ol[@class='documents-list']/li")
result_data = []


for result in results:
    result_title = result.find_element(By.XPATH,".//a").text
    result_url = result.find_element(By.XPATH,".//a").get_attribute("href")
    result_data.append([result_title, result_url])

driver.quit()


# Запись данных в файл CSV
with open("docs_10_years_TINAO.csv", "w", newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Result Title", "URL"])
    writer.writerows(result_data)
