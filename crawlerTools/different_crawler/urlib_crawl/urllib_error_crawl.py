import urllib.error
import urllib.request


class UrllibErrorCrawl(object):
    def errorUrlError(self):
        try:
            url = "http://www.baidus.com"
            resp = urllib.request.urlopen(url)
            print(resp.read().decode('utf-8'))
        # except urllib.error.HTTPError as e:
        #     print("请检查url是否正确")
        # URLError是urllib.request异常的超类
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
if __name__ == '__main__':
    UrllibErrorCrawl().errorUrlError()