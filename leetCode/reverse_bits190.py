class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            res=res<<1 | (n&1)
            n=n>>1
        return res


if __name__=="__main__":
    n=int('00000010100101000001111010011100',base=2)
    print(n)

    print(Solution().reverseBits((n)))
