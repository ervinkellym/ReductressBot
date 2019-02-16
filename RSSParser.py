import feedparser

feed = feedparser.parse("http://reductress.com/rss")

print(len(feed.entries))
print(feed.entries[0].title)
print(feed.entries[0].link)
