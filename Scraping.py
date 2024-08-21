import requests
import re
from bs4 import BeautifulSoup
import Parameter


def main():
    env = Parameter.Parameter()
    website = env.website

    print(website)
    result = requests.get(website)

    # Ensure correct encoding is set
    result.encoding = 'utf-8'

    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    strsoup = str(soup)
    # print(type(str(soup)))

    # print(soup)

    file_path = "./test.html"

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(strsoup)


if __name__ == "__main__":
    main()
