import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("client_id"),
    client_secret=os.getenv("client_secret"),
    user_agent="Wall Street Shits (u/fries)",
)

subreddit = reddit.subreddit("wallstreetbets")

for submission in subreddit.new(limit=10):
    print("Title:", submission.title)
    print("Author:", submission.author)
    print("URL:", submission.url)
    print("Score:", submission.score)
    print("---")