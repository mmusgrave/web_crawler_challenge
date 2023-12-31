import requests
from pprint import pprint
from bs4 import BeautifulSoup
from post import Post

class Crawler:
    def __init__(self, url):
        self.url = url
        self.relevant_post_data = []


    def __extract_relevant_post_data(self, posts, subtext): # List -> List -> List(Dict)
        post_data = []
        for i in range(30):
            post_info = Post(posts[i], subtext[i])
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

    def long_titles_ordered_by_comments(self): # None -> List(Dict)
        long_titles = []
        for post in self.relevant_post_data:
            if len(post.name.split(" ")) > 5:
                long_titles.append(post)

        def get_post_comment_count(post): # Dict -> Int
            return post.comment_count

        long_titles.sort(reverse=True, key=get_post_comment_count)
        return long_titles

    def short_titles_ordered_by_score(self): # None -> List(Dict)
        short_titles = []
        for post in self.relevant_post_data:
            if len(post.name.split(" ")) <= 5:
                short_titles.append(post)

        def get_post_score(post): # Dict -> Int
            return post.score

        short_titles.sort(reverse=True, key=get_post_score)
        return short_titles

if __name__ == '__main__':
    active = True
    crawler = Crawler("https://news.ycombinator.com/")
    crawler.crawl()

    for post in crawler.relevant_post_data:
        post.print_attrs()
    print("These were the 30 most recent posts on YCombinator News")

    while active:
        print()
        print("What else would you like to see?")
        print("You may type the following keywords: ")
        print("1) 'long' to see the long titled posts")
        print("2) 'short' to see the long titled posts")
        print("3) 'refresh' to see the most 30 recent posts on YCombinator News")
        print("4) 'quit' to quit")


        preference = input("Please type your keyword here: ")
        print()
        match preference:
            case "long":
                print("Here are the posts with a title longer than 5 words, ordered by the number of comments: ")
                for post in crawler.long_titles_ordered_by_comments():
                    post.print_attrs()
            case "short":
                print("Here are the posts with a title 5 words or shorter, ordered by their score: ")
                for post in crawler.short_titles_ordered_by_score():
                    post.print_attrs()
            case "refresh":
                print("One second, let me make a new request...")
                crawler.crawl()
                for post in crawler.relevant_post_data:
                    post.print_attrs()
            case "quit":
                print("Quitting time!")
                active = False
            case _:
                print("Please enter an acceptable option next time")

    print("I know you'll come crawling back sooner or later!")
