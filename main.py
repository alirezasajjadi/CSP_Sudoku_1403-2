from CSP.Solver import Solver
from States.StatesProblem import StatesProblem
from Sudoku.SudokuProblem import SudokuProblem




if __name__ == '__main__':

    # states = StatesProblem()
    # s = Solver(states)
    # s.solve()
    # states.print_assignments()

    sudoku = SudokuProblem()
    s = Solver(sudoku)
    s.solve()
    sudoku.print_assignments()
