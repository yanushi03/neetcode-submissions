class Solution:

    def encode(self, strs: List[str]) -> str:
        joined = ""
        for word in strs:
            joined += str(len(word))+"#"+word
        return joined

    def decode(self, s: str) -> List[str]:
        new, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            new.append(s[j+1: j + 1 + length])
            i = j + 1 + length
        return new

    