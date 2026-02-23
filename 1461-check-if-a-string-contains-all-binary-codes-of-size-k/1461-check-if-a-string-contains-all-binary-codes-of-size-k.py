class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < (1 << k):
            return False

        codeSet = [False] * (1 << k)
        cur = 0
        have = 0

        for i in range(n):
            cur = ((cur << 1) & ((1 << k) - 1)) | (ord(s[i]) - ord('0'))

            if i >= k - 1:
                if not codeSet[cur]:
                    codeSet[cur] = True
                    have += 1

        return have == (1 << k)