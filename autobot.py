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

# Automatically update every hour
while(True):
    # Retrieve the most recent submission made to r/ by ReductressBot
    most_recent = 'none'
    for submission in reddit.redditor('ReductressBot').submissions.new(limit=1):
        most_recent = submission.title

    # Find our place in the feed and post everything since then
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

    # Wait 1 hour to check for more updates
    time.sleep(3600)
