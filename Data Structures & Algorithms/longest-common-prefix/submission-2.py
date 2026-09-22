class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix= min(strs)
        new_prefix = [min(strs)]
        for str in strs:
            if len(str) < len(prefix):
                prefix = str
            for i in range(len(prefix)):
                if str[i] != prefix[i]:
                    new_prefix.append(str[:i])
        longest_prefix = min(new_prefix)
        if len(longest_prefix) == 0:
            return ""    
        return "".join(longest_prefix)