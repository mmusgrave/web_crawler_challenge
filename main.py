import requests
from bs4 import BeautifulSoup

# -# Refactors after MVP:
# 1) Make a class for the entries to capture the title, the number of the order,
#    the number of comments, and points for each entry.
#       - Initialise with the html object as arg, use pvt functions for each variable to extract info

URL = "https://news.ycombinator.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

forum_posts = soup.find_all("tr", {"class": "athing"}, limit=30)
# Loop through "forum_posts"
# Create an array of objects with the keys as each attribute
# Create functions to be able to filter for each results

if __name__ == '__main__':
    # Run the script from here
