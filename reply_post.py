import praw
import pdb
import re
import os

# Reddit instance
reddit = praw.Reddit("bot")

# and login
reddit.login("REDDIT_USERNAME", "REDDIT_PASS")

# have we run this code before? if not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
# if we have run this code before, load the list of posts we replied to
else:
    # read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# get the top 5 values from our subreddit
subreddit = reddit.subreddit("name_of_subreddit")
for submission in subreddit.hot(limit=10):
    print(submission.title)

    # if we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # do a case insensitive search
        if re.search("whatever_you_want_to_search", submission.title, re.IGNORECASE):
            # reply to the post
            submission.reply("whatever_you_want_to_reply")
            print("Bot replying to: ", submission.title)

            # store the current id into our list
            posts_replied_to.append(submission.id)

# write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
