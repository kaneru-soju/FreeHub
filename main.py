#! usr/bin/env python3
# import praw
# import pandas as pd
# import datetime as dt
from re import sub
import scraper
#
# # secret keys that we need to hide
# personal_use = '5FghdU95WOsds1gwFy2Gbw'
# secret = 'LlWpk1fsV_0-UFMQXq58xH8atBRxMQ'
#
# # API for praw is here
# # https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html#praw.models.Subreddit
# # create a reddit instance
# reddit = praw.Reddit(client_id=personal_use,
# \
#                      client_secret=secret, \
#                      user_agent='FreeHub', \
#                      username='freeehub', \
#                      password='vthacks9')
#
# # get a subreddit instance
# subreddit = reddit.subreddit('freegames')
# top_subreddit = subreddit.top("week")
#
# # loop through submissions based on the parameters
# # and print the title/id
# for submission in top_subreddit:
#     print(submission.title, submission.id)

subreddit = [scraper.subreddit("freebies", ["[EXPIRED]"], 0.80),
             scraper.subreddit("freegamefindings", ["Expired"], 0.80),
             scraper.subreddit("freestickers", ["EXPIRED"], 0.80),
             scraper.subreddit("freeebooks", ["Expired"], 0.80)]

for sr in subreddit:
    data_harvester = scraper.utils(sr)
    data_harvester.get_valid_posts(sr)
