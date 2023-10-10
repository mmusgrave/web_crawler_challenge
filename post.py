class Post:
    def __init__(self, post_info, subtext):
        self.name = post_info.find("span", {"class": "titleline"}).find("a").get_text()
        self.rank = int(post_info.find("span", {"class": "rank"}).get_text().split('.')[0])
        self.score = int(subtext.find("span", {"class": "score"}).get_text().split(' ')[0])
        comment_count_string = subtext.find_all("a")[-1].get_text().split('\xa0')[0]
        self.comment_count = int(comment_count_string) if comment_count_string != "discuss" else 0
