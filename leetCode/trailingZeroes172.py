class Solution:
    def trailingZeroes(self, n: int) -> int:
        trail_zeroes_num=0
        n=n//5
        while n>0:
            trail_zeroes_num+=n
            n=n//5
        return trail_zeroes_num



    # def trailingZeroes(self, n: int) -> int:
    #     sum=0
    #     total=1
    #     while n>0:
    #         total=total*n
    #         n=n-1
    #     print(total)
    #     while total%10==0:
    #         sum=sum+1
    #         total=total//10
    #     return sum

if __name__=="__main__":
    n=10
    n = 20
    n = 15
    print(Solution().trailingZeroes(n))
