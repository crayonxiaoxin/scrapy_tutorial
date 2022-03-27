# -*- coding = utf-8 -*-
# @Time: 2022/3/27 0027 14:54
# @Author: crayonxiaoxin
# @File: main.py
# @Software: PyCharm

from scrapy.cmdline import execute

# 注意execute的参数类型为一个列表
execute("scrapy crawl quotes".split())
