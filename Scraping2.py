from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import time
from faker import Faker
from Parameter import Parameter as env

fake = Faker()


def get_elements(driver, prefix):
    print("Getting elements with prefix:", prefix)
    li_elements = driver.find_elements(By.TAG_NAME, "li")

    matching = [li for li in li_elements if li.get_attribute(
        'id').startswith(prefix)]

    for element in matching:
        element_id = element.get_attribute('id')
        element_text = element.text
        print(f"Element ID: {element_id}, Text: {element_text}")

        # Open the file in append mode with UTF-8 encoding
        with open("./db/test.txt", "a", encoding="utf-8") as file:
            file.write(f"{element_id}: {element_text}\n")
            print("Element retrieval successful.")


def check_for_block_message(driver):
    try:
        block_message = "ระบบพบว่าคุณใช้โปรแกรมอัตโนมัติในการเข้าใช้งานเว็บไซต์ของเรา"
        if block_message in driver.page_source:
            print("Detected block message on the page. Retrying...")
            return True
        return False
    except Exception as e:
        print("An error occurred while checking for the block message:", str(e))
        return False


def generate_random_history_and_cookies(driver, num_visits=6):
    urls = [
        "https://www.google.com/search?q=" + fake.word(),
        "https://www.facebook.com/" + fake.word(),
        "https://www.chatgpt.com/c/"+fake.word(),
        "https://ntom-api.intense.co.th/",
        "https://javiercbk.github.io/json_to_dart",
        "https://steamdb.info/",
        "https://www.npmjs.com/"
    ]

    for _ in range(num_visits):
        url = random.choice(urls)
        driver.get(url)
        time.sleep(random.uniform(20, 55))

    driver.get("https://www.touchvpn.net/")
    connect_btn = driver.find_element(By.ID, "connect-btn")
    connect_btn.click()
    time.sleep(10)


def main():
    options = Options()
    # options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(executable_path="./chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        for i in range(2, 12):
            print(f"Visiting page {i}...")
            generate_random_history_and_cookies(driver)
            driver.get(env.website + str(i))

            if check_for_block_message(driver):
                time.sleep(5)  # Wait before retrying
                driver.get(env.website + str(i))

            get_elements(driver, "recipe")
            time.sleep(2)

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
