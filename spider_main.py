import url_manager, html_downloader, \
    html_parser, html_outputer

root_url = "http://baike.baidu.com/view/21087.htm"

class SpiderMain(object):
    def __init__(self):
        self.url_manager = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self):
        """爬取网页,并将爬取到的数据保存到html"""
        craw_count = 1  #爬取的次数
        self.url_manager.add_new_url(root_url)
        while self.url_manager.has_new_url():
            try:
                new_url = self.url_manager.get_new_url()
                print("craw 第{0}次 url是{1}".format(craw_count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.url_manager.add_new_urls(new_urls)
                self.outputer.save_data(new_data)

                # 这里只爬取1000次
                if craw_count >= 1000:
                    break

                craw_count += 1
            except Exception as e:
                print('craw failed : {0}', e)

        self.outputer.save_to_html()

if __name__ == '__main__':
    spider = SpiderMain()
    spider.craw()








