import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

if __name__ == '__main__':
    # Run the script from here
