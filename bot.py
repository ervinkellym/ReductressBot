import praw
import pdb
import re
import os

# Create the Reddit instance and log in using praw credentials
# located in local praw.ini file
reddit = praw.Reddit('ReductressBot')

# Pull the hottest 10 entries from r/aww and print the titles
# subreddit = reddit.subreddit('aww')
# for submission in subreddit.hot(limit=10):
#     print(submission.title)

subreddit = reddit.subreddit('reductress')
title = 'Test Post 2 - Please Ignore'
url = 'https://imgur.com/gallery/87dU6iV'
subreddit.submit(title, url=url)
