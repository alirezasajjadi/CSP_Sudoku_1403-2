from Sudoku.SudokuProblem import SudokuProblem
from CSP.Variable import Variable
from Sudoku.KillerSudokuConstraint import KillerCageConstraint

class KillerSudokuProblem(SudokuProblem):
    def __init__(self, board=None, cages=None, name="Killer Sudoku"):
        super().__init__(board=board, name=name)
        if cages is not None:
            for cage_cells, target_sum in cages:
                cage_vars = [self.get_variable_by_position(row, col) for row, col in cage_cells]
                self.constraints.append(KillerCageConstraint(cage_vars, target_sum))

    def get_variable_by_position(self, row: int, col: int) -> Variable:
        index = row * 9 + col
        return self.variables[index]