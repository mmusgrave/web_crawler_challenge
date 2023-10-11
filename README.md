# web_crawler_challenge

This crawler runs exclusively on one URL, https://news.ycombinator.com/. 

It grabs the top 30 posts from that page and extracts 4 values for each post:

1) Rank
2) Name
3) Score
4) Number of Comments

The User can then use 2 filters on the data:
1) Posts with their name longer than 5 words, ordered by the number of comments
2) Posts with their name equal to or shorter than 5 words, ordered by the score

## Usage

This Crawler is used via a CLI. 

Enter your terminal/command line application and navigate to the directory that contains `crawler.py`.

Enter the line `python3 crawler.py` to run the application. 

Follow the instructions given by the application.

## Application Keywords and their Meanings
When using the Crawler CLI, you will have 4 keyword options to choose from to interact with the application. 

1) `long` to see the long titled posts
2) `short` to see the long titled posts
3) `refresh` to see the most 30 recent posts on YCombinator News
4) `quit` to quit
