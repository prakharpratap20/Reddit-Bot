import praw

reddit = praw.reddit("bot")

subreddit = reddit.subreddit("name_of_subreddit")

for submission in subreddit.hot(limit=5):
    print("Title:", submission.title)
    print("Text:", submission.selftext)
    print("Score: ", submission.score)
    print("-----------------------\n")