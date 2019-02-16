import praw
import pdb
import re
import os
import feedparser


# Create a feedparser instance for the Reductress RSS feed
feed = feedparser.parse("http://reductress.com/rss")

# Pull down current entries
num_entries = len(feed.entries)
title = feed.entries[0].title
url = feed.entries[0].link

# Create the Reddit instance and log in using praw credentials
# located in local praw.ini file
reddit = praw.Reddit('ReductressBot')

subreddit = reddit.subreddit('reductress')
subreddit.submit(title, url=url)
