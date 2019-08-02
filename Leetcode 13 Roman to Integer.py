class Solution:
    def romanToInt(self, s: str) -> int:
        runsum = 0
        for i in range(len(s)):
            if s[i] == 'I':
                if i+1<len(s):
                    if s[i+1] == 'X' or s[i+1] == 'V':
                        runsum-=1
                    else:
                        runsum+=1
                else:
                    runsum+=1
            if s[i] == 'V':
                runsum+=5
            if s[i] == 'X':
                if i+1<len(s):
                    if s[i+1] == 'L' or s[i+1] == 'C':
                        runsum -= 10
                    else:
                        runsum += 10
                else:
                    runsum+=10
            if s[i] == 'L':
                runsum += 50
            if s[i] == 'C':
                if i+1<len(s):
                    if s[i+1] == 'D' or s[i+1] == 'M':
                        runsum -= 100
                    else:
                        runsum += 100
                else:
                    runsum += 100
            if s[i] == 'D':
                runsum += 500
            if s[i] == 'M':
                runsum += 1000
        return runsum
