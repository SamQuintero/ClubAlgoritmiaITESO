#https://leetcode.com/problems/rectangle-overlap/description/

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        #izq, der, arr, aba
        return not (rec1[2] <= rec2[0] or rec1[0] >= rec2[2] or rec1[1] >= rec2[3] or rec1[3] <= rec2[1])