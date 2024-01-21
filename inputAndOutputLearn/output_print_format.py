


# 如果有个很长的格式化字符串，不想分割它可以传入一个字典，用中括号( [] )访问它的键；
def dicFormatPrintWithoutSplit():
    table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789789789789}
    print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 'Dcab: {0[Dcab]:d}'.format(table))

def specificWidthFormatPrint():
    table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789}
    for name, phone in table.items(): print('{0:10} ==> {1:10f}'.format(name, phone))

if __name__=="__main__":
    dicFormatPrintWithoutSplit()
    specificWidthFormatPrint()
