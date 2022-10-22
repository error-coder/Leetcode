class Solution:
    def climbStairs(self, n: int) -> int:
        # ex ) n = 4일때 n = 3일때와 n = 2일때 개수를 합하면 n = 4일때의 개수가 같음
        # f(n) = f(n - 1) + f(n - 2)
        # 0으로만 구성된 n만큼의 길이 배열 선언 -> [0] * n
        # f(0) = 0, f(1) = 1, f(2) = 2

        dp = [0,1,2]

        for i in range(3, n + 1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]