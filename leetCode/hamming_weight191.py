class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        for i in range(32):
            if (n & 1) == 1:
                num = num + 1
            n = n >> 1
        return num


if __name__ == "__main__":
    n = int("00000000000000000000000000001011", base=2)
    n = int("00011000000000000000000000001011", base=2)
    n = int("10011000000000000000000000001011", base=2)
    n = int("00000000000000000000000000000000", base=2)
    print(Solution().hammingWeight(n))
