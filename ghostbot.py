#!/usr/bin/python3

import praw

bot= praw.Reddit(
        user_agent="ghostbot12 v0.1",
        client_id="SPOOK12",
        client_secret="superScarySpookr42069",
        username="ghostbot12",
        password= open("pass.txt").read().replace("\n", "")
        )

subreddit= bot.subreddit('me_irl')
comments= subreddit.stream.comments()
SPOOKE_reply= open("genericSPOOK.txt").read()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if 'ghost' in text.lower():
        # Generate a message
        message = SPOOKE_reply
        comment.reply(message) # Send message
