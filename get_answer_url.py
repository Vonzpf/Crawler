#coding:utf-8

import urllib
import re
from bs4 import BeautifulSoup
from bs4.builder._htmlparser import BeautifulSoupHTMLParser
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
    x=0
    for answerurl in urllist:
        urlsplited = answerurl.split('"')
        fullurl = 'https://www.zhihu.com' + urlsplited[1]   #获取完整的答案URL
        
        answerpage = urllib.urlopen(fullurl)
        answerhtml = answerpage.read()
        
        soup = BeautifulSoup(answerhtml,"lxml")
        a_tag = soup.find("div", class_="zm-editable-content clearfix")
        while(a_tag.find_all("noscript")):
            a_tag.noscript.extract()()
        while(a_tag.find_all("br")):
            a_tag.br.decompose()
        answer = a_tag.prettify()
        #获取答案
        
        document = Document()
        document.add_paragraph(answer)
        document.add_page_break()
        document.save('d:\%s.docx' %x)
        x = x + 1

html = getHtml("https://www.zhihu.com/collection/47588314?page=1")

geturl(html)