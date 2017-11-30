"""
笔趣阁的《一念永恒》小说获取
"""
# 用于网络协议的申请
import requests
# 用于对于XML的解析
import xml.etree.cElementTree as ET
from xml.parsers.expat import ParserCreate
from string import Template



class NovelSaxHandler(object):
    # catalogue list handler and define the callback function

    # catalogue list index to save the character information
    cataIndex = 0
    # list object to save the element name
    nameElementNode = []

    def __init__(self, catalogueList):
        self.catalogueList = catalogueList

    def startElement(self, name, attr):
        try:
            self.nameElementNode.append(name)
            if name == 'a':           
                singleElement = {}
                singleElement['elementUrl'] = attr['href']
                self.catalogueList.append(singleElement)
        except expression as identifier:
            print('error')           

    def txtContent(self, text):
        try:
             if self.nameElementNode.__len__()>0 and self.nameElementNode[len(self.nameElementNode)-1] == 'a':
                self.catalogueList[self.cataIndex]['elementTxt'] = text
                print(text)
        except expression as identifier:
             print('error1')

    def endElement(self, name):
        self.nameElementNode.pop()
        if name == 'a':
            self.cataIndex += 1


def getNovelList(urlAddress):
    # get website page content
    content = requests.get(urlAddress).content.decode('gb2312')
    start = content.find('<div id="list">')
    end = content.find('<div id="footer" name="footer">')
    # 截取小说目录列表, 在字符串当中有一些不规则的字符串需要替换掉，如空格的HTML表示方式
    content = content[start:end-8].strip().replace("&nbsp;","")
    
    print(content)

    # novel catalogue list
    cataList = []
    # 生成Sax处理器
    listHandler = NovelSaxHandler(cataList)
    # 初始化分析器
    parser = ParserCreate()
    parser.StartElementHandler = listHandler.startElement
    parser.EndElementHandler = listHandler.endElement
    parser.CharacterDataHandler = listHandler.txtContent
    # 解析数据
    parser.Parse(content)
    return cataList


# 向网站发出请求
reqNovelWebsite = getNovelList("http://www.biquge.com.tw/0_213/")
strTemplate = Template("$elementTxt ($elementUrl)")
for item in reqNovelWebsite:
    print(strTemplate.substitute(elementUrl=item["elementUrl"],elementTxt=item["elementTxt"] ))