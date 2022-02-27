from datetime import date, datetime
from pprint import pprint
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
    def __init__(self, subreddits):
        self.subreddits = subreddits
        self.client: praw.Reddit = praw.Reddit(client_id=personal_use, client_secret=secret, user_agent=user_agent,
                                               username=username, password=password)


    def start_sending_posts(self):
        for submission in self.client.subreddit(self.subreddits).stream.submissions():
            created_at = datetime.fromtimestamp(submission.created_utc)
            now = datetime.utcnow()
            # call the bot.
            if (now - created_at).seconds < (5 * 60):
            # print(submission.subreddit_name_prefixed.split('/')[1])
                print(submission.title + '\n')