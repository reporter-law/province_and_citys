"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
"""
通过国家统计局数据
获取中国所有城市列表
"""
import sys,os,re,requests
from tqdm import tqdm
from lxml import etree
from crawler_tools.user_agent import user_agent as u
class Citys():
    def __init__(self):
        self.url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/"
        self.file = os.path.dirname(__file__)
    def get_url(self):
        header = {
            'Cookie': 'SF_cookie_1=72991020',
            'User-Agent': u.user_agent()["User-Agent"]}
        r1 = requests.get(self.url,headers=header)
        r1.encoding = r1.apparent_encoding
        return r1.text
    def xpath_parse(self,condition):
        #省
        if condition == "provinces":
            lxml = etree.HTML(self.get_url())
            provinces = lxml.xpath("//tr/td/a/text()")
            print("省：", provinces)
            return provinces
        elif condition == "city":
            city = []
            lxml = etree.HTML(self.get_url())
            citys = lxml.xpath("//tr/td/a/@href")
            for n, i in tqdm(enumerate(citys)):
                url = self.url + i
                r2 = requests.get(url, headers=u.user_agent())
                r2.encoding = r2.apparent_encoding
                countys = etree.HTML(r2.text).xpath("//tr/td[2]/a//text()")
                for citys in countys:
                    city.append(citys)
            return city
        elif condition=="zone":
            area = []
            lxml = etree.HTML(self.get_url())
            citys = lxml.xpath("//tr/td/a/@href")
            for n, i in tqdm(enumerate(citys)):
                url = self.url + i
                r2 = requests.get(url, headers=u.user_agent())
                r2.encoding = r2.apparent_encoding
                countys_href = etree.HTML(r2.text).xpath("//tr/td[2]/a/@href")
                for ns, county in enumerate(countys_href):
                    url = self.url+ county
                    print(url)
                    r3 = requests.get(url, headers=u.user_agent())
                    r3.encoding = r3.apparent_encoding
                    zones = etree.HTML(r3.text).xpath("//tr/td[2]/a//text()")
                    for zone in zones:
                        print(zone)
                        area.append(zone)
            return area
        else:
            all = []
            lxml = etree.HTML(self.get_url())
            provinces = lxml.xpath("//tr/td/a/text()")
            citys = lxml.xpath("//tr/td/a/@href")
            for n, i in tqdm(enumerate(citys)):
                url = self.url + i
                r2 = requests.get(url, headers=u.user_agent())
                r2.encoding = r2.apparent_encoding
                citys1 = etree.HTML(r2.text).xpath("//tr/td[2]/a/text()")
                countys_href = etree.HTML(r2.text).xpath("//tr/td[2]/a/@href")
                for ns, county in enumerate(countys_href):
                    url = self.url + county
                    r3 = requests.get(url, headers=u.user_agent())
                    r3.encoding = r3.apparent_encoding
                    zones = etree.HTML(r3.text).xpath("//tr/td[2]/a//text()")
                    for zone in zones:
                        all.append(provinces[n]+","+citys1[ns]+","+zone)
                        print(provinces[n]+","+citys1[ns]+","+zone)
            return all
    def download(self, condition):
        for i in self.xpath_parse(condition=condition):
            with open(self.file + f"\\{condition}.txt", "a+", encoding="utf-8")as f:
                f.write(i + "\n")

Citys().download(condition="zo")
def citys():
    with open(r"J:\PyCharm项目\项目\中国裁判文书网\selenium路线\数据清洗模块\城市（副本）.txt", "r", encoding="utf-8")as f:
        i = 1
        for i_ in f:
            i += 1
        print(i)


