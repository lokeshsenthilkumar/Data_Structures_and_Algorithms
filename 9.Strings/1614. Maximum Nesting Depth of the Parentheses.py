class Solution:
    def maxDepth(self, s):
        mx = c = 0
        for i in s:
            if i == '(':
                c += 1
                mx = max(mx, c)
            if i == ')':
                c -= 1
        return mx