# -*- coding = utf-8 -*-
# @time : 2020/10/7 0:35
# @author : user
# @file : PYTHON3.py
# @software : PyCharm
'''
print("课时，零技术5天搞定PYTHON爬虫技术，并能实现相关数据采集，喜欢的小伙伴多多分享哦~") #这是单行注释
a = 1
print("这是变量：",a)

age = 18
print("我的年纪是: %d岁"%age)
print("我的国籍是%s,我的名字是%s"%("中国","小张"))
print("www","baidu","com",sep=".")
password = input("请输入密码")
print("您刚刚输入的名密码是:",password)

a = input("输入:")

a = int("123")
b = a + 100
print(b)

c = int(input("输入c:"))
print("输入了一个数字:%d"%c)
'''
#BatchInstall.py import os
libs = {"numpy","matplotlib","pillow","sklearn","requests",\
        "jieba","beautifulsoup4","wheel","networkx","sympy",\
        "pyinstaller","django","flask","werobot","pyqt5",\
        "pandas","pyopengl","pypdf2","docopt","pygame"}
try:     for lib in libs:
        os.system("pip3 install "+lib)
     print("Successful")
except:
     print("Failed Somehow")
