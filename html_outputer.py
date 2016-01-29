# 爬虫结果输出到一个html中

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def save_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def save_to_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write('<html>\n')
        fout.write('<meta charset=\'utf-8\'>\n')
        fout.write('<body>\n')
        fout.write('<table border="1">\n')

        for data in self.datas:
            fout.write('<tr>\n')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>\n')

        fout.write('</table>\n')
        fout.write('</body>\n')
        fout.write('</html>\n')

        fout.close()

# 在视频教程里因为文件编码默认为ascii码,所以要对title和summary转编码格式
# 而实际代码中,可以通过将文件格式保存为utf-8,以及在html源码中加上编码信息,就可以正确显示
