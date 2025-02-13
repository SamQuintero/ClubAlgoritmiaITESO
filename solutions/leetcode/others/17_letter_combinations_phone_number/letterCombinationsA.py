#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

#código de Nicolás González
#solución "por fuerza bruta"

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = digits
        l = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []
        lc = []
        
        if len(d) == 0:
            return []
        elif len(d) == 1:
            for i in range(len(l[int(d)])):
                res.append(l[int(d)][i])
        else:
            for i in l[int(d[0])]:
                for j in l[int(d[1])]:
                    if len(d) == 2:
                        comb = "" + i + j
                        res.append(comb)
                    else:
                        for k in l[int(d[2])]:
                            if len(d) == 3:
                                comb = "" + i + j + k
                                res.append(comb)
                            else:
                                for h in l[int(d[3])]:
                                    comb = "" + i + j + k + h
                                    res.append(comb)
        return (res)



    

