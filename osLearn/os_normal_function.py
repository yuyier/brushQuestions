# http://www.ityouknow.com/python/2019/10/09/python-os-demonstration-026.html
import os


class OSNormalFunction(object):

    # os.name
    def osName(self):
        print("os.name:", os.name)

    # os.environ
    def osEnviron(self):
        print("os.environ[\"PATH\"]:", os.environ["PATH"])
        print("os.environ[\"HOMEPATH\"]:", os.environ["HOMEPATH"])
        print("os.environ[\"CLASSPATH\"]:", os.environ["CLASSPATH"])
        print("os.environ[\"OS\"]:", os.environ["OS"])

    def osWalk(self):
        for dirpath, dirnames, filenames in os.walk("C:\Windows"):
            if str(dirpath).__contains__("etc"):
                print("dirpath:", dirpath)
                print("dirnames:", dirnames)
                print("filenames:", filenames)

    def osListdir(self):
        print(os.listdir("E:\Desktop"))

    def osMakdir(self):
        if not os.path.exists("osMakeDir"):
            print(os.mkdir("osMakeDir"))
        if not os.path.exists("osMakeDirs1/hello/hello1"):
            print(os.makedirs("osMakeDirs1/hello/hello1"))

    def osRemove(self):
        if os.path.exists("newOsMakeDir"):
            print(os.rmdir("newOsMakeDir"))
        if os.path.exists("newosMakeDirs1/newhello/newhello1"):
            print(os.removedirs("newosMakeDirs1/newhello/newhello1"))

    def osRename(self):
        if os.path.exists("osMakeDir"):
            print(os.rename("osMakeDir", "newOsMakeDir"))
        if os.path.exists("osMakeDirs1/hello/hello1"):
            print(os.renames("osMakeDirs1/hello/hello1", "newosMakeDirs1/newhello/newhello1"))

    # “getcwd”实际上是“get the current working directory”
    def osGetcwd(self):
        print(os.getcwd())

    def osChdir(self):
        print(os.getcwd())
        print(os.chdir("newOsMakeDir"))
        print(os.getcwd())


if __name__ == "__main__":
    # OSNormalFunction().osName()
    # OSNormalFunction().osEnviron()
    OSNormalFunction().osWalk()
    # OSNormalFunction().osListdir()
    # OSNormalFunction().osMakdir()
    # OSNormalFunction().osRemove()
    # OSNormalFunction().osRename()
    # OSNormalFunction().osGetcwd()
    # OSNormalFunction().osChdir()
