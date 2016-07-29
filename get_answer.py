#coding:utf-8

import urllib
import re
from bs4 import BeautifulSoup
from bs4.builder._htmlparser import BeautifulSoupHTMLParser
from docx import Document
from docx.shared import Inches

def geturl(urllist):
    answerpage = urllib.urlopen(urllist)
    answerhtml = answerpage.read()
        
    soup = BeautifulSoup(answerhtml,"lxml")
    a_tag = soup.find("div", class_="zm-editable-content clearfix")
    while(a_tag.find_all("noscript")):
        a_tag.noscript.extract()()
    while(a_tag.find_all("br")):
        a_tag.br.decompose()
    answer = a_tag.prettify()
    #获取答案
    #print(a_tag.original_encoding)
    
    document = Document()
    document.add_paragraph(answer)
    document.add_page_break()
    document.save('d:\demo.docx')
    
urllist = "https://www.zhihu.com/question/48635051/answer/113194472"
geturl(urllist)