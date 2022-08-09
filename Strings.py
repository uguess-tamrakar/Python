import enum


class Strings:
    def commonChild(s1, s2):
        dp = [0] * (len(s2) + 1)
        for x in range(1, len(s1) + 1):
            prev = 0
            for y in range(1, len(s2) + 1):
                temp = dp[y]
                if (s1[x-1] == s2[y-1]):
                    dp[y] = prev + 1
                else:
                    dp[y] = max(dp[y], dp[y-1])
                prev = temp
        return dp[len(s2)]

