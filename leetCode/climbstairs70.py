class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # return self.f(n)

    # def f(self, n) -> int:
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     return self.f(n - 1) + self.f(n - 2)
