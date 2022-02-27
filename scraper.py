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

    @staticmethod
    def post_is_valid(subreddit, post):
        if post.link_flair_text in subreddit.banned_flairs:
            return False

        return post.upvote_ratio >= subreddit.upvote_threshold

    def get_valid_posts(self, subreddit: subreddit):
        sub = self.client.subreddit(subreddit.name)

        valid_posts = []
        for submission in sub.stream.submissions():
            if self.post_is_valid(subreddit, submission):
                # for now just append the name and and print
                valid_posts.append(submission.title)

        print(valid_posts)
