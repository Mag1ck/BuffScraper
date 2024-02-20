import re
import os
import time
import logging
import winsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Constants
USER_DATA_PATH = '~\\AppData\\Local\\Google\\Chrome\\User Data'
BINARY_LOCATION = r"D:/OneDrive/Pulpit/ESSA/chrome-win64path/chrome.exe"
PRICES_FILE = 'prices.txt'
VALUES_FILE = 'values.txt'
WAIT_TIME = 3
BUY_ORDERS_XPATH = '/html/body/div[6]/div/div[4]/div[1]/ul/li[2]/a'
TRADE_RECORDS_XPATH = '/html/body/div[6]/div/div[4]/div[1]/ul/li[4]/a'

def read_prices():
    """Read prices of items from URLs in PRICES_FILE and write details to VALUES_FILE."""
    # Set the path to your ChromeDriver executable
    chromedriver_path = os.path.join(os.getcwd(), "chromedriver.exe")



    # Create options object
    options = webdriver.ChromeOptions()


    # Use Service class to specify ChromeDriver path
    service = Service(chromedriver_path)

    # Create the Chrome driver instance
    driver = webdriver.Chrome(service=service, options=options)
    try:
        with open(PRICES_FILE, 'r', encoding='utf-8') as f:
            lines = f.read().split("\n")
            for line in lines:
                try:
                    process_item(driver, line.strip())  # Strip to remove leading/trailing whitespace
                except Exception as e:
                    logging.error(f"Error processing item from URL: {line}. Error: {e}")
    except FileNotFoundError:
        logging.error(f"File not found: {PRICES_FILE}")

    driver.quit()





def process_item(driver, url):
    """Process an item from the given URL."""
    driver.get(url)
    time.sleep(WAIT_TIME)

    # Extract item details
    item_name = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/div[1]/h1').text
    lowest_price_element = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[7]/table/tbody/tr[2]/td[5]/div[1]/strong')
    lowest_price = float(re.sub('[¥]+', '', lowest_price_element.text))

    # Navigate to buy orders
    driver.find_element(By.XPATH, BUY_ORDERS_XPATH).click()
    time.sleep(WAIT_TIME)
    first_order_element = driver.find_elements(By.CLASS_NAME, 'f_Strong')[2]
    first_order = float(re.sub('[¥]+', '', first_order_element.text))

    # Navigate to trade records
    driver.find_element(By.XPATH, TRADE_RECORDS_XPATH).click()
    time.sleep(WAIT_TIME)
    prices = [float(re.sub('[¥]+', '', el.text.strip(' '))) for el in driver.find_elements(By.CLASS_NAME, 'f_Strong')[3:]]

    # Calculate average price
    average_price = sum(prices) / len(prices)

    # Check if item meets criteria
    if (first_order / average_price <= 0.85 and lowest_price >= 50) or (lowest_price / average_price <= 0.85 and lowest_price >= 50):
        difference = (lowest_price / average_price) * 100
        winsound.PlaySound(winsound.SND_FILENAME)
        with open(VALUES_FILE, 'a', encoding='utf-8') as file:
            file.write(f"{item_name}\n")
            file.write(f"Cheaper by: {difference:.2f}%\n")
            file.write(f"Link: {url}\n")
            file.write(f"Average price: {average_price:.2f}\n")
            file.write(f"Lowest price: {lowest_price:.2f}\n")
            file.write(f"Lowest buy order: {first_order:.2f}\n")
    logging.info(f"Processed item: {item_name}")


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    read_prices()


if __name__ == "__main__":
    main()
