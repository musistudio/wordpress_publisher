import requests
import json
from bs4 import BeautifulSoup

# 数据获取插件
class GetData():

    def __init__(self):
        self.datas = []

    def getNewsUrl(self):
        url = "http://sports.sina.com.cn/iframe/js/2015/live.js?dpc=1&callback=sports_livecast_hot_list&_=1577435854430"
        res = requests.get(url)
        content = res.text
        content = content[42:-13]
        content = json.loads(content)
        matches = content['matches']
        urls = set()
        for matche in matches:
            url = matche['NewsUrl']
            if url:
                urls.add(url)
        for url in urls:
            self.getNewsContent(url)
        return self.datas


    def getNewsContent(self, url):
        res = requests.get(url)
        content = str(res.content, 'utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.find(class_="second-title").get_text()
        paragraphs = str(soup.find(id="artibody"))
        paragraphs = paragraphs.replace('span', 'div')
        self.datas.append({
            "title": title,
            "content": paragraphs
        })