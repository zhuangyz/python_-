# url管理器,管理未爬取和已爬取的url


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()   #待爬取urls
        self.old_urls = set()   #已爬取urls

    def add_new_url(self, new_url):
        if new_url is None:
            return
        if new_url not in self.new_urls and new_url not in self.old_urls:
            self.new_urls.add(new_url)

    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for new_url in new_urls:
            self.add_new_url(new_url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url






