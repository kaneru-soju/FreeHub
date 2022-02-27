class FreebieInfo:
    def __init__(self, title, image, link, information):
        self.title = title
        self.image = image
        self.link = link
        self.information = information

    def get_title(self):
        return self.title

    def get_image(self):
        return self.image

    def get_link(self):
        return self.link

    def get_information(self):
        return self.information

    def __str__(self):
        return f"{self.title}\n{self.link}\n{self.information}\n{self.image}"


freebie = FreebieInfo("amongus", "sanjana, ", "sunny", "don't self deprecate pls")
print(freebie)
