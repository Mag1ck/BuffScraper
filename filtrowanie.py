import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from filter import filtrowanie


def collect():
    chromedriver_path = os.path.join(os.getcwd(), "chromedriver.exe")

    # Create options object
    options = webdriver.ChromeOptions()

    # Use Service class to specify ChromeDriver path
    service = Service(chromedriver_path)

    # Create the Chrome driver instance
    driver = webdriver.Chrome(service=service, options=options)

    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed

    actual_page = 1
    max_page = 1059

    try:
        with open('prices.txt', 'a', encoding='utf-8') as f:
            while actual_page <= max_page:
                URL = f"https://buff.163.com/market/csgo#tab=selling&page_num={actual_page}"
                driver.get(URL)
                wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))

                lista = driver.find_elements(By.TAG_NAME, "li")
                skins = filter(filtrowanie, lista)

                for i in skins:
                    f.write(i.find_element(By.TAG_NAME, 'a').get_attribute("href") + '\n')

                next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "page-link.next")))
                next_button.click()
                actual_page += 1
    finally:
        driver.quit()


if __name__ == "__main__":
    collect()