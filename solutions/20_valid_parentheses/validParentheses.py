#https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    c2 = stack.pop()
                    if (c == ')' and c2 != '(') or (c == ']' and c2 != '[') or (c == '}' and c2 != '{'):
                        return False
        
        return len(stack) == 0