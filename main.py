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
forum_subtext = soup.find_all("td", {"class": "subtext"}, limit=30)
# Loop through "forum_posts"
# Create an array of objects with the keys as each attribute
# Create functions to be able to filter for each results

post_data = []

for i in range(30):
    # title
    # list_of_things[0].find("span", {"class": "titleline"}).find("a").get_text()
    # order_rank
    # int(list_of_things[0].find("span", {"class": "rank"}).get_text().split('.')[0])
    # comment_count ->
    #  int(list_of_subtext[1].find_all("a")[-1].get_text().split('\xa0')[0])
    # points -> score
    # int(list_of_subtext[0].find("span", {"class": "score"}).get_text().split(' ')[0])
    post_info = {}
    post_info["name"] = forum_posts[i].find("span", {"class": "titleline"}).find("a").get_text()
    post_info["rank"] = int(forum_posts[i].find("span", {"class": "rank"}).get_text().split('.')[0])
    post_info["score"] = int(forum_subtext[i].find("span", {"class": "score"}).get_text().split(' ')[0])
    comment_count_string = forum_subtext[i].find_all("a")[-1].get_text().split('\xa0')[0]
    post_info["comment_count"] = int(comment_count_string) if comment_count_string != "discuss" else 0
    # print(forum_subtext[i].find_all("a")[-1].get_text().split('\xa0')[0])
    # breakpoint()
    # post_info["comment_count"] = int(forum_subtext[i].find_all("a")[-1].get_text().split('\xa0')[0])

    post_data.append(post_info)

# print(post_data)


# if __name__ == '__main__':
#     # Run the script from here
