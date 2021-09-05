class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs[1:]:
            new_prefix = ''
            for letter1, letter2 in zip(prefix, string):
                if letter1 == letter2:
                    new_prefix += letter1
                else:
                    break
            prefix = new_prefix
        return prefix      