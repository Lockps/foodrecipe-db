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

        with open("./db/test.txt", "w") as file:
            element_id + ":" + element_text


def generate_random_history_and_cookies(driver, num_visits=6):
    urls = [
        "https://www.google.com/search?q=" + fake.word(),
        "https://www.facebook.com/asdasswasc/",
        "https://www.chatgpt.com/",
        "https://ntom-api.intense.co.th/",
        "https://javiercbk.github.io/json_to_dart",
        "https://steamdb.info/",
        "https://www.npmjs.com/"
    ]

    for _ in range(num_visits):
        url = random.choice(urls)
        driver.get(url)
        time.sleep(random.uniform(2, 5))


def main():
    options = Options()
    # options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(executable_path="./chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        for i in range(1, 12):
            print(i)
            generate_random_history_and_cookies(driver)
            driver.get(env.website+str(i))
            get_elements(driver, "recipe")
            print("Element retrieval successful.")
            time.sleep(2)

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
