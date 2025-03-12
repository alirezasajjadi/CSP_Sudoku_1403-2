from CSP.Solver import Solver
from Sudoku.SudokuProblem import SudokuProblem
from Sudoku.KillerSudokuProblem import KillerSudokuProblem
from Sudoku.KillerKnightSudokuProblem import KillerKnightSudokuProblem


board = [
    [0, 2, 3, 0, 5, 6, 7, 0, 0],
    [4, 0, 6, 7, 0, 9, 1, 0, 0],
    [7, 8, 0, 1, 0, 3, 0, 0, 6],
    [0, 0, 4, 0, 6, 0, 0, 9, 1],
    [5, 6, 7, 8, 0, 0, 2, 3, 0],
    [0, 9, 0, 0, 3, 4, 5, 0, 7],
    [3, 0, 0, 6, 0, 0, 0, 1, 2],
    [6, 0, 8, 9, 1, 2, 0, 0, 0],
    [9, 1, 0, 3, 4, 0, 6, 7, 0]  
]


cages = [
    ([(0, 0), (0, 1)], 3),  
    ([(0, 2), (0, 3)], 7),  
    ([(0, 4), (0, 5)], 11),  
    ([(0, 6), (0, 7), (0, 8)], 24),  

    ([(1, 0), (1, 1), (1, 2)], 15),  
    ([(1, 3), (1, 4), (1, 5)], 24),  
    ([(1, 6), (1, 7), (1, 8)], 6),  

    ([(7, 0), (7, 1)], 13),  
    ([(7, 2), (7, 3)], 17),  
    ([(7, 4), (7, 5)], 3),  
    ([(7, 6), (7, 7), (7, 8)], 12),  

    ([(8, 0), (8, 1)], 10),  
    ([(8, 2), (8, 3), (8, 4)], 9), 
    ([(8, 5), (8, 6), (8, 7), (8, 8)], 26),  
]

if __name__ == "__main__":
    
    print("\nTesting Killer Sudoku solver...")
    killer = KillerSudokuProblem(board=board, cages=cages)
    solver = Solver(killer)
    solver.solve()
    killer.print_assignments()

    print("\nTesting Killer Knight Sudoku solver...")
    killer_knight = KillerKnightSudokuProblem(board=board, cages=cages, knight=True)
    solver = Solver(killer_knight)
    solver.solve()
    killer_knight.print_assignments()
