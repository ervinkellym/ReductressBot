import praw
import pdb
import re
import os
import feedparser
import time
import io
import json

# @Author Laurel Romoser and Kelly Ervin
# @Date 06/12/2019

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


# Open queue.txt file as json file and load file
queue = []
last_bat = ""
with open('queue.txt') as json_file:
    data = json.load(json_file)
    queue = data["queue"]
    last_bat = data["last_bat_title"]

curr_bat = entries[0].title

# Check first that the RSS feed has a new batch of articles. Only update the
# queue if new articles are present
if curr_bat != last_bat:
    # If queue is empty, add everything from the reverse feed to the queue that
    # hasn't already been posted
    if len(queue) == 0:
        caught_up = False
        for entry in reversed(entries):
            if entry.title == most_recent:
                caught_up = True
            else:
                if caught_up:
                    queue.append((entry.title, entry.link))
                else:
                    continue

        # In case the whole RSS feed does not contain our most recently posted
        # article title
        if not caught_up:
            for entry in reversed(entries):
                queue.append((entry.title, entry.link))
    else:
        # Otherwise grab the last item title in the queue
        last = queue[len(queue) - 1][0]
        # loop through reverse feed, don't add entries to the queue until we hit
        # the last item
        caught_up = False
        for entry in reversed(entries):
            if entry.title == last:
                caught_up = True
            else:
                # append the rest of the reverse feed to the queue
                if caught_up:
                    queue.append((entry.title, entry.link))
                else:
                    continue
        # In case the whole RSS feed does not contain our last item
        if not caught_up:
            for entry in reversed(entries):
                queue.append((entry.title, entry.link))

# Post the top entry from queue and delete
subreddit.submit(queue[0][0], url=queue[0][1])
queue.pop(0)

# Write the queue back to the queue.txt file
with open('queue.txt', 'w') as write_file:
    data = {}
    data["queue"] = queue
    data["last_bat_title"] = curr_bat
    text = json.dumps(data, indent=4)
    write_file.write(text)
