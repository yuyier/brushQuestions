

class ExceptionLearn(object):
    def tryExceptFinally(self,val1,val2):
        # print()
        print("----start caculate----")
        try:
            result=val1/val2
            print(result)
        except ValueError as e:
            print("ValueError:",e)
        except ZeroDivisionError as e:
            print("ZeroDivisionError:",e)
        except Exception as e:
            print("exception:",e)
        finally:
            print("always excute this finally block!!")
        print("----end caculate----")
        print()

    def getAge(self):
        age=input('please input age:')
        if 140>=int(age)>=1:
            return int(age)
        raise ValueError('the age you input is not between the 1 and 140')

    def raiseException(self):
        try:
            age=self.getAge()
            print('input age is ',age)
        except ValueError as e:
            print(e)

    def getScore(self):
        s=input('请输入学生成绩（0~100）:')
        score=int(s)
        assert 0<=score<=100,'the input score need to be between 0~100'
        return score

    def assertException(self):
        try:
            self.getScore()
        except ValueError as e:
            print(e)
        except AssertionError as e:
            print(e)







if __name__=="__main__":
    ExceptionLearn().tryExceptFinally(10,2)
    ExceptionLearn().tryExceptFinally("10",2)
    ExceptionLearn().tryExceptFinally(10,0)
    ExceptionLearn().tryExceptFinally(10.11,0)
    while input("Continue to input age?(Yes/No)")=="Yes":
        ExceptionLearn().raiseException()

    while input("Continue to input Score?(Yes/No)") == "Yes":
        ExceptionLearn().assertException()