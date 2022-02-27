import asyncio
from datetime import date, datetime
from random import randint

import praw
from FreebieInfo import FreebieInfo
from config import personal_use, secret, username, user_agent, password


class subreddit:

    def __init__(self, name, banned_flairs, ts):
        self.name = name
        self.banned_flairs = banned_flairs
        self.upvote_threshold = ts


class utils:

    # subreddit object
    # exclusion flair, etc.,
    def __init__(self, bot, subreddits):
        self.dclient = bot
        self.subreddits = subreddits
        self.client: praw.Reddit = praw.Reddit(client_id=personal_use, client_secret=secret, user_agent=user_agent,
                                               username=username, password=password)

    async def start_sending_posts(self):
        for submission in self.client.subreddit(self.subreddits).stream.submissions():
            created_at = datetime.fromtimestamp(submission.created_utc)
            now = datetime.utcnow()
            # call the bot.
            if (now - created_at).seconds > (5 * 60):
                post_subreddit = submission.subreddit_name_prefixed.split('/')[1]
                await self.dclient.post_freebie(FreebieInfo(submission.title, submission.thumbnail, submission.url,
                                                            submission.link_flair_css_class, post_subreddit,
                                                            submission.upvote_ratio))
                await asyncio.sleep(randint(2, 5))
