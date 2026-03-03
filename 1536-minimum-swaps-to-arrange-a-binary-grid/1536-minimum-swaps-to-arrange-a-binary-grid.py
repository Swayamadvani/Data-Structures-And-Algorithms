class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        Find minimum number of row swaps to make the grid upper triangular.
        An upper triangular matrix has all elements below the main diagonal as 0.
      
        Args:
            grid: n x n binary matrix
          
        Returns:
            Minimum number of swaps needed, or -1 if impossible
        """
        n = len(grid)
      
        # Find the rightmost 1 position in each row
        # This tells us how many trailing zeros each row has
        rightmost_one_positions = [-1] * n
      
        for row_idx in range(n):
            for col_idx in range(n - 1, -1, -1):
                if grid[row_idx][col_idx] == 1:
                    rightmost_one_positions[row_idx] = col_idx
                    break
      
        total_swaps = 0
      
        # For each row position, find a suitable row that can be placed there
        for target_row in range(n):
            # Find the first row from current position onwards that can fit
            # A row can fit at position i if its rightmost 1 is at position <= i
            suitable_row_idx = -1
          
            for candidate_row in range(target_row, n):
                if rightmost_one_positions[candidate_row] <= target_row:
                    # Found a suitable row
                    total_swaps += candidate_row - target_row
                    suitable_row_idx = candidate_row
                    break
          
            # If no suitable row found, it's impossible to form upper triangular matrix
            if suitable_row_idx == -1:
                return -1
          
            # Bubble the suitable row up to the target position
            # This simulates the actual row swaps
            while suitable_row_idx > target_row:
                rightmost_one_positions[suitable_row_idx], rightmost_one_positions[suitable_row_idx - 1] = \
                    rightmost_one_positions[suitable_row_idx - 1], rightmost_one_positions[suitable_row_idx]
                suitable_row_idx -= 1
      
        return total_swaps