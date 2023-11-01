import praw
import re
import random

chandler_quotes = [
    "I'm not so good with the advice... Can I interest you in a sarcastic comment?",
    "Could I BE any more...?",
    "I'm Chandler, could I BE any more...?",
    "My two greatest assets have been my humility and my breasts.",
    "Well, I don't have your talent, I can't make the sound of a woman having multiple orgasms.",
    "I don't have a pla...wait, wait, I do have a plan!",
    "Until I was 25, I thought the response to 'I love you' was 'Oh, crap!'",
    "You hide my clothes, I'm getting naked.",
    "Oh, the sorrow. The sorrow!",
    "I'm not great at the advice. Can I interest you in a sarcastic comment?",
    "Well, they should tell you, y'know, it's like a contest. With concrete!",
    "It's like all my life everyone always told me, 'You're a shoe! You're a shoe! You're a shoe!' Well, what if I don't want to be a shoe? What if I want to be a purse, you know, or a hat!",
    "I make jokes when I'm uncomfortable.",
    "Oh... my... God!",
    "You have to stop the Q-tip when there's resistance!",
    "Gum would be perfection.",
    "Could I BE more confused?",
    "We were on a break!",
    "My wallet's too small for my fifties, and my diamond shoes are too tight!",
    "I'm not great at the advice. Can I interest you in a sarcastic comment?"
]

reddit = praw.Reddit("bot")

subreddit = reddit.subreddit("ProgrammerHumor")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("Chandler", comment.body, re.IGNORECASE):
        chandler_reply = "Chandler: " + random.choice(chandler_quotes)
        comment.reply(chandler_reply)
        print(chandler_reply)