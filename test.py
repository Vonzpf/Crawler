#coding=utf-8

import urllib
import re

from docx import Document
from docx.shared import Inches


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def geturl(html):
    reg = r'data-entry-url=".+"'
    urlre = re.compile(reg)
    urllist = re.findall(urlre,html)
    print(urllist)

html = getHtml("https://www.zhihu.com/collection/47588314?page=1")

geturl(html)
