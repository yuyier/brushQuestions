# 第一步使用urllib库获取网页
# 第二步使用BeautifulSoup和re库解析数据:定位数据块、使用正则解析数据块
# 将数据导出excel
import http.client

import requests
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
import xlwt
from crawler_common_function import CrawlerCommonFunction

class DoubanCrawler(object):
    # 定义基础url，发现规律，每页最后变动的是start=后面的数字
    baseurl = "https://movie.douban.com/top250?start="
    # 定义正则对象获取指定的内容
    # 提取链接（链接的格式都是<a href="开头的）
    findLink = re.compile(r'<a href="(.*?)">')
    # 提取图片
    findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让 '.' 特殊字符匹配任何字符，包括换行符；
    # 提取影片名称
    findTitle = re.compile(r'<span class="title">(.*)</span>')
    # 提取影片评分
    findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
    # 提取评价人数
    findJudge = re.compile(r'<span>(\d*)人评价</span>')
    # 提取简介
    inq = re.compile(r'<span class="inq">(.*)</span>')
    # 提取相关内容
    findBd = re.compile(r'<p class="">(.*)</p>(.*)<div', re.S)



    # 定义一个函数，并解析这个网页
    def analysisDataDouBanTop250(self,baseurl):
        # 定义接收10页的列表
        dataList = []
        # 获取指定网页
        for i in range(0, 10):  # 获取网页选项的函数，10次
            url = baseurl + str(i * 25)
            html = CrawlerCommonFunction().getUrlContent(url,CrawlerCommonFunction().getUrlType["htmlType"])
            # 指定解析器解析html,得到BeautifulSoup对象
            soup = BeautifulSoup(html)
            # 定位我们的数据块在哪
            for item in soup.find_all('div', class_="item"):
                # item 是 bs4.element.Tag 对象，这里将其转换成字符串来处理
                item = str(item)
                # 定义一个列表 来存储每一个电影解析的内容
                data = []
                # findall返回的是一个列表，这里提取链接
                link = re.findall(self.findLink, item)[0]
                data.append(link)  # 添加链接
                img = re.findall(self.findImgSrc, item)[0]
                data.append(img)  # 添加图片链接
                title = re.findall(self.findTitle, item)
                # 一般都有一个中文名 一个外文名
                if len(title) == 2:
                    # ['肖申克的救赎', '\xa0/\xa0The Shawshank Redemption']
                    titlename = title[0] + title[1].replace(u'\xa0', '')
                else:
                    titlename = title[0] + ""
                data.append(titlename)  # 添加标题
                pf = re.findall(self.findRating, item)[0]
                data.append(pf)
                pjrs = re.findall(self.findJudge, item)[0]
                data.append(pjrs)
                inqInfo = re.findall(self.inq, item)
                if len(inqInfo) == 0:
                    data.append(" ")
                else:
                    data.append(inqInfo[0])
                bd = re.findall(self.findBd, item)[0]
                # [('\n                            导演: 弗兰克·德拉邦特 Frank Darabont\xa0\xa0\xa0主演: 蒂姆·罗宾斯 Tim Robbins /...<br/>\n                            1994\xa0/\xa0美国\xa0/\xa0犯罪 剧情\n                        ', '\n\n                        \n                        ')]
                bd[0].replace(u'\xa0', '').replace('<br/>', '')
                bd = re.sub('<\\s*b\\s*r\\s*/\\s*>', "", bd[0])
                bd = re.sub('(\\s+)?', '', bd)
                data.append(bd)
                dataList.append(data)
        return dataList



    def doubanMainCrawler(self):
        save_dataList=self.analysisDataDouBanTop250(self.baseurl)
        save_path = "E:\\Desktop\\ChenLiqingInterviewPrepare\\Coding\\brushQuestions\\crawlerTools\\download_file\\DouBan250_1.xls"
        igm_path= "E:\\Desktop\\ChenLiqingInterviewPrepare\\Coding\\brushQuestions\\crawlerTools\\download_img\\"
        col_name = ("电影详情链接", "图片链接", "电影中/外文名", "评分", "评论人数", "概况", "相关信息")
        sheet_name = "豆瓣电影Top250"
        col_num=7
        line_num=250
        need_download_img=False
        CrawlerCommonFunction().excelSave(sheet_name, col_name, col_num, line_num, save_path, save_dataList,need_download_img,igm_path)


if __name__ == "__main__":
    DoubanCrawler().doubanMainCrawler()