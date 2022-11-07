class Solution:
    def maximum69Number(self, num: int) -> int:
        m = num
        s = (str(num))
        for i in range(len(s)):
            if s[i] == "6":
                temp = (int(s[:i]+"9"+s[i+1:]))
            else:
                temp = (int(s[:i]+"6"+s[i+1:]))
            m = max(m, temp)
        return m
