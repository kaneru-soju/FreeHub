class FreebieInfo:
    def __init__(self, title, image, link, information, subreddit, upvote):
        self.title = title
        self.image = image
        self.link = link
        self.information = information
        self.subreddit = subreddit
        self.upvote = upvote

    def get_title(self):
        return self.title

    def get_image(self):
        return self.image

    def get_link(self):
        return self.link

    def get_information(self):
        return self.information

    def get_subreddit(self):
        return self.subreddit

    def get_upvote(self):
        return self.upvote

    def __str__(self):
        return f"{self.title}\n{self.link}\n{self.information}\n{self.image}\n{self.subreddit}\n{self.upvote}"