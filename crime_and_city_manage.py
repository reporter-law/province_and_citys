"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
from tqdm import tqdm
crimes,cities = [],[]
with open(r"J:\PyCharm项目\项目\中国裁判文书网\selenium路线\文书爬取模块\获取城市限定模块\常见刑法罪名.txt","r",encoding="utf-8")as f:
    for i in f.readlines():
        i = i.strip()
        crimes.append(i)
with open(r"J:\PyCharm项目\项目\中国裁判文书网\selenium路线\文书爬取模块\获取城市限定模块\city.txt","r",encoding="utf-8")as f_:
    for i in f_.readlines():
        i = i.strip()
        cities.append(i)
years = ["2019-12-01"]
for i in range(1,13):
    if len(str(i))==1:
        a = f"2020-0{i}-01"
    else:
        a = f"2020-{i}-01"
    years.append(a)
print(years)



for i in tqdm(list(set(crimes))):
    for i_ in list(set(cities)):
        for index,year in enumerate(years):
            with open(r"J:\PyCharm项目\项目\中国裁判文书网\selenium路线\文书爬取模块\获取城市限定模块\crime_and_cities.txt", "a",encoding="utf-8")as f1:
                if index+1 <= len(years)-1:
                    f1.write(i_+","+i+","+year+","+years[index+1]+"\n")
                else:
                    f1.write(i_ + "," + i + ","+year + "," + "2021-02-01" + "\n")



