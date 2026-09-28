class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # Found the whole word
            if i == len(word):
                return True

            # Out of bounds / already used / wrong character
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in path or
                word[i] != board[r][c]
            ):
                return False

            # Choose this cell
            path.add((r, c))

            # Try all 4 directions
            res = (
                dfs(r, c + 1, i + 1) or  # right
                dfs(r, c - 1, i + 1) or  # left
                dfs(r + 1, c, i + 1) or  # down
                dfs(r - 1, c, i + 1)     # up
            )

            # Undo / backtrack
            path.remove((r, c))

            return res

        # Try starting from every cell
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False