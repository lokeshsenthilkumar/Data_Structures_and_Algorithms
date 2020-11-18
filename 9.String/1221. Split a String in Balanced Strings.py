from itertools import accumulate
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return list(accumulate(1 if i=='R' else -1 for i in s)).count(0)