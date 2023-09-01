class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            max_sum = k
        elif (k - numOnes) <= numZeros:
            max_sum = numOnes
        else:
            max_sum = numOnes - (k - numOnes - numZeros)
        return max_sum
