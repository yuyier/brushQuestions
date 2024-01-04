import urllib.parse


class UrllibParseCrawl(object):
    def urllibParseUrlparse(self):
        url = "http://www.example.com:80/path/to/myfile.html?key1=value&key2=value2#SomewhereIntheDocument"
        parsed_result = urllib.parse.urlparse(url)
        print(parsed_result)
        print('协议-scheme  :', parsed_result.scheme)
        print('域名-netloc  :', parsed_result.netloc)
        print('路径-path    :', parsed_result.path)
        print('路径参数-params  :', parsed_result.params)
        print('查询参数-query   :', parsed_result.query)
        print('片段-fragment:', parsed_result.fragment)
        print('用户名-username:', parsed_result.username)
        print('密码-password:', parsed_result.password)
        print('主机名-hostname:', parsed_result.hostname)
        print('端口号-port    :', parsed_result.port)

    def urllibParseUrlsplit(self):
        url = "http://www.example.com:80/path/to/myfile.html?key1=value&key2=value2#SomewhereIntheDocument"
        # urlsplit分割，唯一的区别就是不会把params拆分出来
        parsed_result = urllib.parse.urlsplit(url)
        print(parsed_result)
        print('协议-scheme  :', parsed_result.scheme)
        print('域名-netloc  :', parsed_result.netloc)
        print('路径-path    :', parsed_result.path)
        # parsed_result.params 没有这项
        print('查询参数-query   :', parsed_result.query)
        print('片段-fragment:', parsed_result.fragment)
        print('用户名-username:', parsed_result.username)
        print('密码-password:', parsed_result.password)
        print('主机名-hostname:', parsed_result.hostname)
        print('端口号-port    :', parsed_result.port)

    def urllibParseUrldefrag(self):
        url = "http://www.example.com:80/path/to/myfile.html?key1=value&key2=value2#SomewhereIntheDocument"
        parsed_result = urllib.parse.urldefrag(url)
        print(parsed_result)
        # DefragResult(url='http://www.example.com:80/path/to/myfile.html?key1=value&key2=value2', fragment='SomewhereIntheDocument')
        url1 = "http://www.example.com:80/path/to/myfile.html?key1=value&key2=value2"
        parsed_result1 = urllib.parse.urldefrag(url1)
        print(parsed_result1)

    def urllibParseUrlunparse(self):
        url_compos = ('http', 'www.example.com:80', '/path/to/myfile.html', 'params2', 'query=key1=value&key2=value2',
                      'SomewhereIntheDocument')
        print(urllib.parse.urlunparse(url_compos))

    def urllibParseUrljoin(self):
        print(urllib.parse.urljoin('https://movie.douban.com/', 'index'))
        print(urllib.parse.urljoin('https://movie.douban.com/', 'https://accounts.douban.com/login'))

    def urllibParseUrlencode(self):
        query_args = {
            'name': 'dark sun',
            'country': '中国'
        }
        query_args = urllib.parse.urlencode(query_args)
        print(query_args)

    def urllibParseParse_qs(self):
        query_args = {
            'name': 'dark sun',
            'country': '中国'
        }
        query_args = urllib.parse.urlencode(query_args)
        print(query_args)  # name=dark+sun&country=%E4%B8%AD%E5%9B%BD

        print(urllib.parse.parse_qs(query_args))  # 返回字典
        print(urllib.parse.parse_qsl(query_args))  # 返回列表




if __name__=="__main__":
    #UrllibParseCrawl().urllibParseUrlparse()
    # UrllibParseCrawl().urllibParseUrlsplit()
    # UrllibParseCrawl().urllibParseUrldefrag()
    # UrllibParseCrawl().urllibParseUrlunparse()
    # UrllibParseCrawl().urllibParseUrljoin()
    # UrllibParseCrawl().urllibParseUrlencode()
    UrllibParseCrawl().urllibParseParse_qs()