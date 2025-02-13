#https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
#from math import gcd

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums), max(nums))