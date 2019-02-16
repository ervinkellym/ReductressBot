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
# subreddit.submit(title, url=url)

# Fill in current article backlog - remove after 1 successful run
subreddit.submit(feed.entries[1].title, url=feed.entries[1].link)
subreddit.submit(feed.entries[2].title, url=feed.entries[2].link)
subreddit.submit(feed.entries[3].title, url=feed.entries[3].link)
subreddit.submit(feed.entries[4].title, url=feed.entries[4].link)
subreddit.submit(feed.entries[5].title, url=feed.entries[5].link)
subreddit.submit(feed.entries[6].title, url=feed.entries[6].link)
subreddit.submit(feed.entries[7].title, url=feed.entries[7].link)
subreddit.submit(feed.entries[8].title, url=feed.entries[8].link)
subreddit.submit(feed.entries[9].title, url=feed.entries[9].link)
