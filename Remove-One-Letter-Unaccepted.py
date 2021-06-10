class Solution:
    def solve(self, s0, s1):
        nl = []
        for i in range(len(s0)):
            nl.append(s0[:i]+s0[i+1:])
        if s1 in nl:
            return True
        else:
            return False