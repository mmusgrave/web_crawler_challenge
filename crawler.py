import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, url):
        self.url = url
        self.relevant_post_data = []


    def __extract_relevant_post_data(self, posts, subtext): # List -> List -> List(Dict)
        post_data = []

        for i in range(30):
            post_info = {}

            post_info["name"] = posts[i].find("span", {"class": "titleline"}).find("a").get_text()
            post_info["rank"] = int(posts[i].find("span", {"class": "rank"}).get_text().split('.')[0])
            post_info["score"] = int(subtext[i].find("span", {"class": "score"}).get_text().split(' ')[0])
            comment_count_string = subtext[i].find_all("a")[-1].get_text().split('\xa0')[0]
            post_info["comment_count"] = int(comment_count_string) if comment_count_string != "discuss" else 0

            post_data.append(post_info)

        return post_data


    def crawl(self): # None -> List(Dict)
        # Make GET request for page info and parse it with BeautifulSoup
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")

        # Uses BeautifulSoup to get all relevant post information from 2 places
        forum_posts = soup.find_all("tr", {"class": "athing"}, limit=30)
        forum_subtext = soup.find_all("td", {"class": "subtext"}, limit=30)

        # Saves data in member variable for class instance for late use
        self.relevant_post_data = self.__extract_relevant_post_data(forum_posts, forum_subtext)

        # Returns relevant data
        return self.relevant_post_data

if __name__ == '__main__':
    crawler = Crawler("https://news.ycombinator.com/")
    crawler.crawl()
    print(crawler.relevant_post_data)
