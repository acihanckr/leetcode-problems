import re
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(words, key = len, reverse = True)
        s = words[0]+'#'
        for word in words[1:]:
            if s.find(word+'#') == -1:
                s = s+word+'#'
        return len(s)