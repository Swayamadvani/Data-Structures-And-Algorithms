class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res, part = [], []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        n = len(digits)

        def dfs(i):
            if i >= n:
                res.append("".join(part))
                return

            for letter in mapping[digits[i]]:
                part.append(letter)
                dfs(i + 1)
                part.pop()

        dfs(0)
        return res
        