#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import urllib.request
import requests
import random
import lxml.html
#from lxml import etree
from bs4 import BeautifulSoup
from rich.console import Console

proxies = {
    "http": "http://127.0.0.1:8889",
    "https": "http://127.0.0.1:8889",
}
console = Console()


#print(response.text)
#response = urllib.request.urlopen('https://docs.python.org/zh-cn/3/howto/urllib2.html')
#html = response.read()
#print(html.decode('utf-8'))
def get_wisdom():
    response = requests.get(
        "https://zh.m.wikiquote.org/wiki/Wikiquote:%E9%A6%96%E9%A1%B5",
        proxies=proxies)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    td = soup.find_all('td')
    console.print(td[4].text, style="bold green")


def get_verse():
    response = requests.get("https://v1.jinrishici.com/all.txt")
    response.encoding = 'utf-8'
    console.print(response.text, style="bold green")


def get_news():
    response = requests.get("https://zh.wikiredia.com/")
    response.encoding = 'utf-8'
    html = lxml.html.fromstring(response.text)
    #html = etree.parse(response.text)
    data = html.xpath('//ul')
    info = data[6].xpath('string(.)')
    console.print("新闻动态", style="bold blue")
    console.print(info, style="bold green")


def get_history():
    response = requests.get("https://zh.wikiredia.com/")
    response.encoding = 'utf-8'
    html = lxml.html.fromstring(response.text)
    #html = etree.parse(response.text)
    data = html.xpath('//dl')
    info = data[1].xpath('string(.)')
    console.print("历史上的今天", style="bold blue")
    console.print(info, style="bold green")


def get_dog():
    response = requests.get("https://we.dog/")
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    td = soup.find_all('article')
    console.print(td[0].text, style="bold green")

def get_ewisdom():
    response = requests.get("https://en.wikiquote.org/wiki/Main_Page",proxies=proxies)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    td = soup.find_all('td')
    console.print(td[3].text, style="bold green")
def get_proverb():
    response = requests.get("https://zh.m.wikiquote.org/wiki/%E4%B8%AD%E6%96%87%E8%B0%9A%E8%AF%AD",proxies=proxies) 
    response.encoding = 'utf-8'
    #print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    li = soup.find_all('li')
    #print(type(li))
    rand = random.randint(15,651)
    console.print(li[rand].text, style="bold green")


#wisdom()
if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-w', '--wisdom', action='store_true', help='每日名言')
    parse.add_argument('-v', '--verse', action='store_true', help='随机诗句')
    parse.add_argument('-n', '--news', action='store_true', help='每日新闻')
    parse.add_argument('-his', '--history', action='store_true', help='历史上的今天')
    parse.add_argument('-d', '--dog', action='store_true', help='舔狗日记')
    parse.add_argument('-ew', '--ewisdom', action='store_true', help='英文每日名言')
    parse.add_argument('-p', '--proverb', action='store_true', help='中文谚语')
    args = parse.parse_args()
    if args.wisdom == True:
        get_wisdom()
    elif args.verse == True:
        get_verse()
    elif args.news == True:
        get_news()
    elif args.history == True:
        get_history()
    elif args.dog == True:
        get_dog()
    elif args.ewisdom == True:
        get_ewisdom()
    elif args.proverb == True:
        get_proverb()    
