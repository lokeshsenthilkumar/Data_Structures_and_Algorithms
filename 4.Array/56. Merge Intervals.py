class Solution:
    def merge(self, intervals):
        l = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if l and i[0] <= l[-1][1]:
                l[-1][1] = max(l[-1][1], i[1])
            else:
                l.append(i)
        return l