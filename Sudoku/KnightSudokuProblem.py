from Sudoku.SudokuProblem import SudokuProblem
from States.StatesConstraint import StatesNotSameConstraint

class KnightSudokuProblem(SudokuProblem):
    def __init__(self, board=None, name="Knight Sudoku"):
        super().__init__(board=board, name=name)
        self.add_knight_constraints()

    def add_knight_constraints(self):
        """Add constraints for all pairs of cells a knight's move apart."""
        for i in range(81):
            row = i // 9
            col = i % 9
            neighbors = self.get_knight_neighbors(row, col)
            for n_row, n_col in neighbors:
                j = n_row * 9 + n_col
                if j > i:  
                    var1 = self.variables[i]
                    var2 = self.variables[j]
                    self.constraints.append(StatesNotSameConstraint([var1, var2]))

    def get_knight_neighbors(self, row: int, col: int) -> list[tuple[int, int]]:
        """Return valid knight's move positions from (row, col)."""
        moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        neighbors = []
        for dr, dc in moves:
            r = row + dr
            c = col + dc
            if 0 <= r < 9 and 0 <= c < 9:
                neighbors.append((r, c))
        return neighbors