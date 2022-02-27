import praw
from config import personal_use, secret, username, user_agent, password


class subreddit:

    def __init__(self, name, banned_flairs, ts):
        self.name = name
        self.banned_flairs = banned_flairs
        self.upvote_threshold = ts


class utils:

    # subreddit object
    # exclusion flair, etc.,
    def __init__(self, subreddit):
        self.subreddit = subreddit
        self.client: praw.Reddit = praw.Reddit(client_id=personal_use, client_secret=secret, user_agent=user_agent,
                                               username=username, password=password)


    def start_sending_posts(self, reddits):
        sub = self.client.subreddit(reddits)
        valid_posts = []

        for submission in sub.stream.submissions():
            # call the bot.
            pass

        print(valid_posts)
