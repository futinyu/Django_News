# coding = gbk

import requests
import re
from lxml import html
import sys
from bs4 import BeautifulSoup
import json

from lxml.html.clean import unicode


class news():
    def __init__(self):
        self.newTitle = []
        self.newDate = []
        self.newLabel = []
        self.newImage = []
        self.newContent = []
        self.newDes = []
        self.newOrigin = []

    def get_content(self, url):
        origin = ''
        content = requests.get(url).content.decode('gbk', 'ignore')
        selector = html.fromstring(content)
        artical_source = selector.xpath('//*[@id="ne_article_source"]/text()')
        for i in artical_source:
            origin += i

        # if not selector.xpath('//*[@id="endText"]'):
        #     info = ''
        # else:
        #     text = selector.xpath('//*[@id="endText"]')[0]
        #     info = text.xpath('string(.)')

        soup = BeautifulSoup(content, 'lxml')
        if not soup.find(id="endText"):
            info = ''
        else:
            info = u''.join([str(x) for x in soup.find(id="endText").contents]).strip()

        if not selector.xpath('//*[@id="endText"]'):
            des = ''
        else:
            text = selector.xpath('//*[@id="endText"]')[0]
            des = text.xpath('string(.)')
            des = re.split(r'。|！', des)[0].replace(' ', '').replace('\n', '')
        return origin, info, des

    def get_page(self, url):
        newTitle = []
        newDate = []
        newLabel = []
        label = []
        l = ''
        newImage = []
        newContent = []
        newDes = []
        newOrigin = []

        header = {
            'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        source_json = requests.get(url, headers=header).content.decode('gbk', 'ignore')
        source_json = source_json.replace('data_callback', '').replace('(', '').replace(')', '')
        source_data = json.loads(source_json)

        title = re.findall(r'"title":"(.*?)"', source_json.replace(' ', ''), re.S)
        for each in title:
            newTitle.append(each)

        time = re.findall(r'"time":"(.*?)"', source_json, re.S)
        for each in time:
            newDate.append(each)

        image = re.findall(r'"imgurl":"(.*?)"', source_json.replace(' ', ''), re.S)
        for each in image:
            newImage.append(each)

        for dict in source_data:
            keynwords = dict['keywords']
            label.append(keynwords)
        for each in label:
            for i in each:
                l += i['keyname'] + ' '
            newLabel.append(l)
            l = ''

        cotent_url = re.findall(r'"docurl":"(.*?)"', source_json.replace(' ', ''), re.S)
        for i_url in cotent_url:
            origin, info, des = self.get_content(i_url)
            newOrigin.append(origin)
            newContent.append(info)
            newDes.append(des)

        self.newTitle = newTitle
        self.newDate = newDate
        self.newLabel = newLabel
        self.newImage = newImage
        self.newContent = newContent
        self.newDes = newDes
        self.newOrigin = newOrigin

# guonei_new = news()
# guonei_new.get_page('https://temp.163.com/special/00804KVA/cm_guonei.js?callback=data_callback')
# for i in range(0, len(guonei_new.newTitle)):
#     print(sys.getsizeof(guonei_new.newImage[i]))
