from pprint import pprint


class Solution:
    def fib(self, n, i=0, a=0, b=1):
        if i == n:
            return a
        return self.fib(n=n, i=i + 1, a=b, b=a + b)


if __name__ == '__main__':
    s = Solution()
    n = 8
    print(s.fib(n=n))
