from CSP.Problem import Problem
from CSP.Variable import Variable
from Sudoku.SudokuConstraint import SudokuConstraint


class SudokuProblem(Problem):
    def __init__(self, board=None, name="Sudoku"):
        if board is None:
            board = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
        
        variables = []
        for row in range(9):
            for col in range(9):
                domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                initial_value = board[row][col] if board[row][col] not in [0, None] else None
                var = Variable(domain, f"cell_{row}_{col}", initial_value)
                variables.append(var)
        
        constraints = []
        
        for row in range(9):
            row_vars = [variables[row * 9 + col] for col in range(9)]
            constraints.append(SudokuConstraint(row_vars))
        
        for col in range(9):
            col_vars = [variables[row * 9 + col] for row in range(9)]
            constraints.append(SudokuConstraint(col_vars))
        
        # (3x3 grids)
        for box_row in range(3):
            for box_col in range(3):
                box_vars = []
                for row in range(3):
                    for col in range(3):
                        var_row = box_row * 3 + row
                        var_col = box_col * 3 + col
                        box_vars.append(variables[var_row * 9 + var_col])
                constraints.append(SudokuConstraint(box_vars))
        
        super().__init__(constraints, variables, name)
    
    def print_assignments(self):
        """
        Print the Sudoku board in a readable format.
        """
        print(f"\n{self.name}")
        print("-" * 25)
        for row in range(9):
            row_str = ""
            for col in range(9):
                var = self.variables[row * 9 + col]
                value = var.value if var.has_value else 0
                if col % 3 == 0:
                    row_str += "| "
                row_str += f"{value} "
            row_str += "|"
            print(row_str)
            if (row + 1) % 3 == 0:
                print("-" * 25)