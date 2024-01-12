# http://www.ityouknow.com/python/2019/10/09/python-os-demonstration-026.html
import os


class OsPathModule(object):
    def osPathjoin(self):
        print(os.path.join("just", "do", "python", "dot", "com"))
        print(os.path.join("just", "do", "d:\\", "python", "dot", "com"))
        print(os.path.join("just", "do", "d:\\", "python", "dot", "g:\\", "com"))

    def osPathAbspath(self):
        print(os.path.abspath("a:/just/do/python"))
        # 绝对路径是当前运行脚本的路径
        print( os.path.abspath("exception_learn.py"))

    # 该函数返回传入路径的“基名”，即传入路径的最下级目录。
    def osPathBasename(self):
        print(os.path.basename("a:/just/do/python"))
        print( os.path.basename("exception_learn.py"))
        print(os.path.basename("a:/just/do/python/"))

    # 与上一个函数正好相反，返回的是最后一个分隔符前的整个字符串
    def osPathDirname(self):
        print(os.path.dirname("a:/just/do/python"))
        print( os.path.dirname("exception_learn.py"))
        print(os.path.dirname("a:/just/do/python/"))

    # 将传入路径以最后一个分隔符为界，分成两个字符串，并打包成元组的形式返回

    def osPathSplit(self):
        print(os.path.split("a:/just/do/python"))
        print(os.path.split("exception_learn.py"))
        print(os.path.split("a:/just/do/python/"))

    # 判断路径所指向的位置是否存在。若存在则返回True，不存在则返回False
    def osPathExists(self):
        print(os.path.exists("a:/just/do/python"))
        print(os.path.exists("exception_learn.py"))
        print(os.path.exists("os_path_module.py"))
        print(os.path.exists("../exceptionLearn/exception_learn.py"))

    # 函数判断传入路径是否是绝对路径，若是则返回True，否则返回False。当然，仅仅是检测格式，同样不对其有效性进行任何核验
    def osPathIsabs(self):
        print(os.path.isabs("a:/just/do/python"))
        print(os.path.isabs("exception_learn.py"))
        print(os.path.isabs("os_path_module.py"))
        print(os.path.isabs("../exceptionLearn/exception_learn.py"))

    # 判断传入路径是否是文件，并且校验有效性
    def osPathIsfile(self):
        print(os.path.isfile("a:/just/do/python"))
        print(os.path.isfile("a:/just/do/python/"))
        print(os.path.isfile("exception_learn.py"))
        print(os.path.isfile("E:\\Desktop\\ChenLiqingInterviewPrepare\\Coding\\brushQuestions\\osLearn\\os_path_module.py"))
        print(os.path.isfile("../exceptionLearn/exception_learn.py"))

    # 判断传入路径是否是路径，并且校验有效性
    def osPathIsdir(self):
        print(os.path.isdir("a:/just/do/python"))
        print(os.path.isdir("a:/just/do/python/"))
        print(os.path.isdir("exception_learn.py"))
        print(os.path.isdir("E:\\Desktop\\ChenLiqingInterviewPrepare\\Coding\\brushQuestions\\osLearn\\os_path_module.py"))
        print(os.path.isdir("../exceptionLearn/exception_learn.py"))
        print(os.path.isdir("../exceptionLearn/"))


if __name__=="__main__":
    # OsPathModule().osPathjoin()
    # OsPathModule().osPathAbspath()
    # OsPathModule().osPathBasename()
    # OsPathModule().osPathDirname()
    # OsPathModule().osPathSplit()
    # OsPathModule().osPathExists()
    OsPathModule().osPathIsabs()
    # OsPathModule().osPathIsfile()
    # OsPathModule().osPathIsdir()