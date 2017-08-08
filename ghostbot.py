#!/usr/bin/python3

import praw
import time
import traceback
from multiprocessing import Pool
import random

bot= praw.Reddit(
        user_agent="ghostbot12 v0.1",
        client_id="62c9efcMBeyfQw",
        client_secret=open("secret.txt").read().replace("\n",""),
        username="ghostbot12",
        password= open("pass.txt").read().replace("\n", "")
        )

SPOOKE_reply= open("genericSPOOK.txt", encoding="UTF-8").read()

def check4SPOOP(comment):
    wordlist= open('wordlist.txt', encoding="UTF-8").read().splitlines()
    authorlist= open('authorlist.txt', encoding="UTF-8").read().splitlines()
    try:
        if any([w in comment.body.lower() for w in wordlist]):
            return True
        elif any([a in comment.author.name for a in authorlist]):
            return True
        elif random.randint(0,99)==69:
            return True
        else:
            print(".", end='')
            return False
    except:
        print("I got SPOOKD while looking at a comment.")
        traceback.print_exc()

def spookstream(subname):
    subreddit= bot.subreddit(subname)
    comments= subreddit.stream.comments()
    for comment in comments:
        if check4SPOOP(comment):
            message = SPOOKE_reply
            print("\nabout to SPOOP ", comment.author.name)
            t= time.localtime()
            print(
                    t.tm_year,"-",t.tm_mon,"-",t.tm_mday,"_",
                    t.tm_hour,":",t.tm_min,":",t.tm_sec,
                    t.tm_zone,
                    sep=''
                    )
            print(comment.link_permalink)
            try:
                comment.reply(message) # Send message
                print("SPOOKD", comment.author.name, "\n")
            except:
                print("Failed 2 SPOOK!")
                traceback.print_exc()

            wait= float(open("wait.txt").read())
            time.sleep(wait)


#pool= Pool()
#pool.apply_async(spookstream, 'me_irl')
spookstream('me_irl')
