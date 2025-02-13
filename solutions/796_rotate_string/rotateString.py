#https://leetcode.com/problems/rotate-string/description/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return False if len(s) != len(goal) else goal in (s + s)