#https://leetcode.com/problems/unique-paths/description/
@cache #decorador que nos ahorra el trabajo de almacenar los valores de retorno ya calculados para (n, r) ya enviados como argumentos
#algoritmo basado en el triángulo de Pascal para calcular combinaciones de n elementos en r espacios
def combinations(n, r):
    if r == 0 or n == r: #casos base
        return 1
    else: #caso recursivo
        return combinations(n-1, r) + combinations(n-1, r-1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        return combinations(m + n, n)