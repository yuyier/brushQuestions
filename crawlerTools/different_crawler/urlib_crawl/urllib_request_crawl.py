import urllib.request
from urllib import request


class UrllibRequestCrawl(object):
    def urlopenCrawlBaidu(self):
        url = "http://www.baidu.com"
        res = request.urlopen(url)
        print(dir(res))
        bye = res.read()
        # print(dir(bye))
        print(bye.decode("utf-8"))
        print(res.status, res.version, res.url, res.reason, res.info, res.headers)

    def urlopenCrawlGet(self):
        url = "http://httpbin.org/get"
        res = urllib.request.urlopen(url)
        print(res.read().decode("utf-8"))

    def urlopenCrawlPost(self):
        url = "http://httpbin.org/post"
        data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
        res = urllib.request.urlopen(url, data=data)
        print(res.read().decode("utf-8"))

    def urlopenCrawlFakeHeader(self):
        url = "http://douban.com"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)

        print(resp.read().decode('utf-8'))

    def urlopenCrawlTimeOut(self):
        url = "http://httpbin.org/get"
        try:
            print(dir(urllib))
            resp = urllib.request.urlopen(url, timeout=0.01)
            print(resp.read().decode('utf-8'))

        except urllib.error.URLError as e:
            print(e)

    def callback(seft, blocknum, blocksize, totalsize):
        """
            @blocknum:目前为此传递的数据块数量
            @blocksize:每个数据块的大小，单位是byte,字节
            @totalsize:远程文件的大小
        """
        if totalsize == 0:
            percent = 0
        else:
            percent = blocknum * blocksize / totalsize
        if percent > 1.0:
            percent = 1.0
        percent = percent * 100
        print("download : %.2f%%" % (percent))

    def urlRequestRetrieve(self):
        url = "http://www.hao6v.com/"
        filename = "E:\\Desktop\\ChenLiqingInterviewPrepare\\Coding\\brushQuestions\\crawlerTools\\download_file\\film1.html"
        local_filename, headers = urllib.request.urlretrieve(url, filename, self.callback)
        print(local_filename, headers)


if __name__ == '__main__':
    print("hello")
    # UrllibRequestCrawl().urlopenCrawlBaidu()
    # UrllibRequestCrawl().urlopenCrawlGet()
    # UrllibRequestCrawl().urlopenCrawlPost()
    # UrllibRequestCrawl().urlopenCrawlFakeHeader()
    # UrllibRequestCrawl().urlopenCrawlTimeOut()
    UrllibRequestCrawl().urlRequestRetrieve()
