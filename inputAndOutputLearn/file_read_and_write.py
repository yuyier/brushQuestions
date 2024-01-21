'''要读取文件内容，调用 read(size) ，size为可选参数'''

'''一次性读取文件所有内容'''
def file_read(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        file_str = file.read(5)
        print(file_str)
        file.close()

'''readline()
读取一行，换行符为 \n 。'''
def file_readline(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_str = file.readline()
        print(file_str)
        file.close()

'''readlines()
读取文件中包含的所有行，可设置可选参数 size 。'''
def file_readlines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_str = file.readlines(0)
        print(file_str)
        file.close()

'''write()
write(string) 将 string 的内容写入文件。'''
def file_write(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file_str = file.write("hahaha")
        print(file_str)
        file.close()

'''seek(offset, from_what) 改变文件当前的位置。offset 移动距离；from_what 起始位置，0 表示开头，1 表示当前位置，2 表示结尾，默认值为 0 ，即开头'''
def file_seek(file_path):
    with open(file_path, 'rb+') as file:
        file.write(b"eeehahaha")
        file.seek(2)
        print(file.read())
        file.close()
'''tell() 返回文件对象当前所处的位置，它是从文件开头开始算起的字节数。'''
def file_tell(file_path):
    with open(file_path, 'rb+') as file:
        file.write(b"eeehahaha")
        file.seek(2)
        print(file.tell())
        print(file.read())
        file.close()

if __name__ == "__main__":
    file_path = "E:\\Desktop\\ChenLiqingInterviewPrepare\\Coding\\brushQuestions\\README.md"
    # file_read(file_path)
    # file_readline(file_path)
    # file_readlines(file_path)
    file_write(file_path)
    # file_seek(file_path)
    # file_tell(file_path)
