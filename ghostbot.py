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
wordlist= open('wordlist.txt', encoding="UTF-8").read().splitlines()
authorlist= open('authorlist.txt', encoding="UTF-8").read().splitlines()

def check4SPOOP(comment):
    global wordlist
    global authorlist
    if wordlist in comment.body.lower():
        return True
    elif authorlist in comment.author.name:
        return True
    else:
        return False

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if check4SPOOP(comment):
        # Generate a message
        message = SPOOKE_reply
        print("about to SPOOP ", comment.author.name)
        comment.reply(message) # Send message
        print("SPOOKD", comment.author.name, "\n")
        time.sleep(60)
