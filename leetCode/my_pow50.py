class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x,n)



if __name__=="__main__":
    # x,n=2,2
    # x, n = 2, -2
    x = 2.00000
    n = 10
    print(Solution().myPow(x,n))