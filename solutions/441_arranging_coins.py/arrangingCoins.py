'''
Referencia al problema:
https://leetcode.com/problems/arranging-coins/description/
'''
def arrangeCoins(n):
    i = 1
    count = 0 
    while(n-i >= 0):
           
        n -= i
        i += 1
        count += 1
    
    return count

n = int(input())
res = arrangeCoins(n)
print(res)