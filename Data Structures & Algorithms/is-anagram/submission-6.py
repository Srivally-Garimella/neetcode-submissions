class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        sh, th = {}, {}
        for i in s:
            sh[i] = sh.get(i,0)+1
        for j in t:
            th[j] = th.get(j,0)+1
        return sh == th
            