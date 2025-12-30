class Solution:
    def removeStars(self, s):
        res = []
        for c in s:
            if c != '*':
                res += c
            elif res:
                res.pop()
        return ''.join(res)


if __name__ == '__main__':
    sol = Solution()
    args = "leet**cod*e"
    print(sol.removeStars(args))
