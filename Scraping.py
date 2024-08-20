import requests
from bs4 import BeautifulSoup
import Parameter


def main():
    env = Parameter.Parameter()
    website = env.website

    print(website)


if __name__ == "__main__":
    main()
