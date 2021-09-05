class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        else:
            print(str(x))
            if str(x) == str(x)[::-1]:
                return True
            else:
                return False