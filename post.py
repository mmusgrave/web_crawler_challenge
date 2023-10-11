from bs4 import BeautifulSoup

class Post:
    def __init__(self, post_info, subtext):
        self.name = post_info.find("span", {"class": "titleline"}).find("a").get_text()
        self.rank = int(post_info.find("span", {"class": "rank"}).get_text().split('.')[0])

        score_span = subtext.find("span", {"class": "score"})
        if score_span != None:
            self.score = int(score_span.get_text().split(' ')[0])
        else:
            self.score = 0

        comment_count_string = subtext.find_all("a")[-1].get_text().split('\xa0')[0]
        if comment_count_string != "discuss" and comment_count_string != "hide":
            self.comment_count = int(comment_count_string)
        else:
            self.comment_count = 0

    def print_attrs(self):
        rank_string = "Rank " + str(self.rank) + ". "
        score_string = "Score: " + str(self.score) + ", "
        comment_count_string = "Number of Comments: " + str(self.comment_count)
        print(rank_string + self.name + ", " + score_string + comment_count_string)
