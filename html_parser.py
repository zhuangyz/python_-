# 页面解析器
# 解析出要爬取的数据
from bs4 import BeautifulSoup   # 关于BeautifulSoup,可以查看它的官方文档
import re       #正则表达式
import urllib.parse     #url操作的


class HtmlParser(object):

    def __init__(self):
        pass

    def parse(self, url, html_content):
        if url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        parsed_urls = self.parsed_new_urls(url, soup)
        parsed_data = self.parsed_new_data(url, soup)

        return parsed_urls, parsed_data

    def parsed_new_urls(self, url, soup):
        new_urls = set()    # 解析得到的url

        # 百度百科中的关联链接是这样的格式:/view/123.htm,用正则表达式找出这些链接
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        # 因为这些链接不完整,需要拼接上百度百科的前缀
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def parsed_new_data(self, url, soup):
        """
        解析出title和简介
        返回值为字典,包含url,title,summary
        """
        result_data = {}

        result_data['url'] = url

        # 标题的html标签格式是<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        # 所以将按照这种格式查找
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        result_data['title'] = title_node.get_text()

        # 简介的html格式是<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        result_data['summary'] = summary_node.get_text()

        return result_data




