"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
from tqdm import tqdm
crimes,cities = [],[]
with open(r"J:\PyCharm项目\项目\中国裁判文书网\selenium路线\法条内容提取\罪名与法定刑\刑法罪名.txt","r")as f:
    for i in f.readlines():
        i = i.strip()
        crimes.append(i)
with open(r"J:\PyCharm项目\项目\中国裁判文书网\selenium路线\数据清洗模块\城市（副本）.txt","r",encoding="utf-8")as f_:
    for i in f_.readlines():
        i = i.strip()
        cities.append(i)
for i in tqdm(crimes):
    for i_ in cities:
        with open(r"J:\PyCharm项目\项目\中国裁判文书网\selenium路线\文书爬取模块\crime_and_cities.txt", "a",encoding="utf-8")as f1:
            f1.write(i+","+i_+"\n")



