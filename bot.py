import praw
import pdb
import re
import os
import feedparser
import time

# Create a feedparser instance for the Reductress RSS feed
feed = feedparser.parse("http://reductress.com/rss")
entries = feed.entries

# Create the Reddit instance and log in using praw credentials
# located in local praw.ini file
reddit = praw.Reddit('ReductressBot')
subreddit = reddit.subreddit('reductress')

# Retrieve the most recent submission made to r/Reductress by ReductressBot
most_recent = 'none'
for submission in reddit.redditor('ReductressBot').submissions.new(limit=1):
    most_recent = submission.title

# Post everything until we hit the last article we posted from the feed
caught_up = False
for entry in reversed(entries):
    if entry.title == most_recent:
        caught_up = True
    else:
        if caught_up:
            subreddit.submit(entry.title, url=entry.link)
            time.sleep(5) # So Reddit doesn't think we are spamming
        else:
            continue
