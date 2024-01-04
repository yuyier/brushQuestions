# import bs4.BeautifulSoup
from bs4 import BeautifulSoup


class UrllibBeautifulSoupCrawl(object):
    def beautifulSoup(self):
        soup1 = BeautifulSoup(open("E:\\Desktop\\ChenLiqingInterviewPrepare\\Coding\\brushQuestions\\crawlerTools\\download_file\\film.html"))
        print(dir(soup1))
        print(soup1.get_text())


if __name__=="__main__":
    UrllibBeautifulSoupCrawl().beautifulSoup()
