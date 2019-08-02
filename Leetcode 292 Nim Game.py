class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= 3:
            return bool(True)

        if n%4 == 0:
            return bool(False)
        else:
            return bool(True)
        
