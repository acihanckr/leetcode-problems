class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            reverse_int = -int(str(x)[:0:-1])
            if reverse_int>-2**31 and reverse_int< 2**31-1:
                return reverse_int
            else:
                return 0
        else:
            reverse_int = int(str(x)[::-1])
            if reverse_int>-2**31 and reverse_int< 2**31-1:
                return reverse_int
            else:
                return 0