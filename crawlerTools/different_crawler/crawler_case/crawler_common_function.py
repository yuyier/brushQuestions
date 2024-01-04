from urllib import request
from urllib import error
from http import client

import xlwt


class CrawlerCommonFunction(object):
    getUrlType = {"htmlType": 1, "imgType": 2}

    # 定义一个函数getHtmlByURL, 得到指定url网页的内容
    def getUrlContent(self,url,urlType):
        # 自定义headers(伪装，告诉豆瓣服务器，我们是什么类型的机器,以免被反爬虫)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        # 利用Request类来构造自定义头的请求
        req = request.Request(url, headers=headers)
        try:
            # urlopen()方法的参数，发送给服务器并接收响应
            resp = request.urlopen(req)
            # urlopen()获取页面内容，返回的数据格式为bytes类型，需要decode()解码，转换成str类型
            respContent = ''
            if urlType == 1:
                respContent = resp.read().decode("utf-8")
            if urlType == 2:
                respContent = resp.read()
        except error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
        except client.IncompleteRead as e:
            print(e)
        return respContent


    def imgDownload(self,img_url, img_name, img_path):
        resp = self.getUrlContent(img_url, self.getUrlType["imgType"])
        img_path = img_path+ str(img_name).split("/")[0] + '.jpg'
        # 将图片写入指定位置
        try:
            with open(img_path, 'wb') as f:
                f.write(resp)
        except Exception as e:
            print(e)


    def excelSave(self,sheet_name,col_name,col_num,line_num,save_path,save_dataList,need_download_img,igm_path):
        book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建Workbook对象
        sheet = book.add_sheet(sheet_name, cell_overwrite_ok=True)  # 创建工作表
        print(len(save_dataList))
        for i in range(0, col_num):
            sheet.write(0, i, col_name[i])
        for i in range(0, line_num):
            print('正在保存第' + str((i + 1)) + '条')
            data = save_dataList[i]
            for j in range(len(data)):
                sheet.write(i + 1, j, data[j])
                # if j==1:
            if need_download_img:
                self.imgDownload(data[1], data[2],igm_path)

        book.save(save_path)