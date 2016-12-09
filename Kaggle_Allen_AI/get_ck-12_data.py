__author__ = 'Administrator'
#-*-coding:utf8-*-
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class spider(object):

    def getsource(self,url):
        html = requests.get(url)
        return html.text
    def geteveryclass(self,source):
        everyclass = re.findall('(<h3>.*?</h3>)',source,re.S)
        return everyclass
    def getinfo(self,eachclass):
        info = re.search('title="(.*?)">',eachclass,re.S).group(1).strip()
        return info
    def saveinfo(self,classinfo):
        f = open('ck-12.txt','a')
        for each in classinfo:
            f.writelines(each + '\n')
        f.close()

if __name__ == '__main__':
    classinfo = []
    url = ['https://www.ck12.org/earth-science/', 'http://www.ck12.org/life-science/', 'http://www.ck12.org/physical-science/', 'http://www.ck12.org/biology/', 'http://www.ck12.org/chemistry/', 'http://www.ck12.org/physics/']
    ck_12_spider = spider()

    for link in url:
        print  'doing: '+ link
        html = ck_12_spider.getsource(link)
        everyclass = ck_12_spider.geteveryclass(html)
        for each in everyclass:
            info = ck_12_spider.getinfo(each)
            classinfo.append(info)
    ck_12_spider.saveinfo(classinfo)



