#!/usr/bin/python3

import praw
import time

bot= praw.Reddit(
        user_agent="ghostbot12 v0.1",
        client_id="62c9efcMBeyfQw",
        client_secret=open("secret.txt").read().replace("\n",""),
        username="ghostbot12",
        password= open("pass.txt").read().replace("\n", "")
        )

subreddit= bot.subreddit('me_irl')
comments= subreddit.stream.comments()
SPOOKE_reply= open("genericSPOOK.txt", encoding="UTF-8").read()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if 'ghost' in text.lower():
        # Generate a message
        message = SPOOKE_reply
        print("about to SPOOP ", comment.author.name)
        print("\n")
        comment.reply(message) # Send message
        print("SPOOKD", comment.author.name, "\n")
        time.sleep(60)
