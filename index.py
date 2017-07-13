__author__ = 'seekxy'
import urllib
import urllib.request
from bs4 import BeautifulSoup
import pymysql
"""
    1.抓取糗事百科所有纯文本段子
    2.保存的本地文件
"""
class QiuShi():
        def __init__(self):
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            self.headers = {'User-Agent':user_agent}

        def query(self,page=1):
            self.url = 'http://www.qiushibaike.com/text/page/' + str(page)
            print(self.url)
            res = urllib.request.Request(self.url,headers=self.headers)
            html = urllib.request.urlopen(res)
            bsoup = BeautifulSoup(html,'html.parser')
            for content in bsoup.find_all('div',{'class':'content'}):
                sql = "INSERT INTO articles (content) VALUES ( '%s' )"
                data = (content.get_text())
                cursor.execute(sql % data)
                print(content.get_text())

if __name__ =='__main__':
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='test',
        charset="utf8"
    )
    cursor = conn.cursor()
    qiushi = QiuShi()
    for i in range(35):
        qiushi.query(i)

    cursor.close()
    conn.commit()
    conn.close()