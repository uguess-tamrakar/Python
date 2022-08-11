class Strings:
    def commonChild(s1, s2):
        dp = [0] * (len(s2) + 1)
        for x in range(1, len(s1) + 1):
            prev = 0
            for y in range(1, len(s2) + 1):
                temp = dp[y]
                if s1[x - 1] == s2[y - 1]:
                    dp[y] = prev + 1
                else:
                    dp[y] = max(dp[y], dp[y - 1])
                prev = temp
        return dp[len(s2)]

    def areBalancedBrackets(s):
        # balanced brackets must have even size (open-closed brackets)
        if len(s) % 2 != 0:
            return False
        stack = []
        open_bracs = ["[", "{", "("]
        for idx, c in enumerate(s):
            if open_bracs.__contains__(c):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                lastItem = stack.pop()
                if (
                    (lastItem == "[" and c != "]")
                    or (lastItem == "{" and c != "}")
                    or (lastItem == "(" and c != ")")
                ):
                    return False
        return True if len(stack) == 0 else False
