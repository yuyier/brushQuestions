import os


class SearchMkdirRmdirInComputer(object):

    # file_path:指定搜索的目录
    # search_file_name:指定搜索文件的关键字
    def searchFile(self,file_path,search_file_name):
        for root_path,file_dir,file_name in os.walk(file_path):
            for file in file_name:
                if file.__contains__(search_file_name):
                    print(root_path,file)

    def mkDir(seft,path):
        """
        创建文件夹
        :param path:
        :return:
        """
        path = path.strip()
        path = path.rstrip('\\')
        isExist = os.path.exists(path)
        if not isExist:
            os.mkdir(path)
            return True
        else:
            return False

    def removeDir(seft,path):
        """
        创建文件夹
        :param path:
        :return:
        """
        path = path.strip()
        path = path.rstrip('\\')
        isExist = os.path.exists(path)
        if isExist:
            os.rmdir(path)
            return True
        else:
            return False


if __name__=="__main__":
    # file_path="E:\\Desktop\\"
    # search_file_name=".ppt"
    # SearchMkdirRmdirInComputer().searchFile(file_path,search_file_name)
    # mk_path = "E:\\Desktop\\newfile"
    # print("make new file:",SearchMkdirRmdirInComputer().mkDir(mk_path))
    rm_path = "E:\\Desktop\\newfile"
    print("make new file:", SearchMkdirRmdirInComputer().removeDir(rm_path))