
class Strings:

    def isPalindrome(s):
        n = len(s)
        if n == 1:
            return True
        mid = n // 2
        left = mid - 1
        right = mid if n % 2 == 0 else mid + 1
        
        while left >= 0 and right < n:
            if s[left] != s[right]:
                return False
            left -= 1
            right += 1
        return True

    def commonChild(s1, s2):
        # memo = [0] * len(s2)
        # for x in range(len(s1)):
        #     previous = 0
        #     for y in range(len(s2)):
        #         temp = memo[y]
        #         if (s1[x] == s2[y]):
        #             memo[y] = previous + 1
        #         else:
        #             memo[y] = max(memo[y], memo[y-1] if y > 0 else 0)
        #         previous = temp
        # return memo[len(s2) - 1]
        n, m = len(s1), len(s2)
        lcs = [[0] * (m + 1) for _ in range(n + 1)]

        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                if c1 == c2:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

        return lcs[n - 1][m - 1]

    

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
