import requests


class WebsiteUpdater:
    def __init__(self, url):
        self.url = url;

    def post(self, post_data: dict):
        request = requests.post(self.url, data=post_data)
        print(request.text)
        print(f'Status Code: {request.status_code}')


websiteUpdater = WebsiteUpdater("http://ptsv2.com/t/91zdd-1645849874")
websiteUpdater.post({"test": "bruh"})
