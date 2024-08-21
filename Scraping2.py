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
    print("get element")
    li_elements = driver.find_elements(By.TAG_NAME, "li")

    matching = [li for li in li_elements if li.get_attribute(
        'id').startswith(prefix)]

    print(matching)


def generate_random_history_and_cookies(driver, domain, num_visits=3):
    urls = [
        "https://www.google.com/search?q=" + fake.word(),
        "https://www.facebook.com/asdasswasc/",
        "https://www.tweethunter.io",
        "https://www.chatgpt.com/",
        "https://ntom-api.intense.co.th/",
        "https://javiercbk.github.io/json_to_dart",
        "https://steamdb.info/",
        "https://www.npmjs.com/"
    ]

    for _ in range(num_visits):
        url = random.choice(urls)
        driver.get(url)
        time.sleep(random.uniform(2, 5))  # Simulate user delay

        # # Generate a random cookie
        # cookie = {
        #     'name': fake.word(),
        #     'value': fake.word(),
        #     'domain': domain,
        #     'path': '/',
        #     # Expiry time (1 hour to 1 day)
        #     'expiry': int(time.time()) + random.randint(3600, 86400)
        # }
        # driver.add_cookie(cookie)

    cookies = driver.get_cookies()
    print("Generated cookies:")
    for cookie in cookies:
        print(cookie)


def main():
    options = Options()
    options.add_argument("--headless")

    service = Service(executable_path="./chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        generate_random_history_and_cookies(driver, domain=env.website)

        driver.get(env.website)

        get_elements(driver, "recipe")

        time.sleep(2000)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
