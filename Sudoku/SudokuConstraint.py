from CSP.Constraint import Constraint
from CSP.Variable import Variable

class SudokuConstraint(Constraint):
    """
    A constraint that ensures all variables in a group (row, column, or box) have different values.
    """
    def __init__(self, variables: list[Variable]):
        super().__init__(variables)
    
    def is_satisfied(self) -> bool:
        """
        Get all assigned variables and check whether they have different values
        """
        assigned_vars = [var for var in self.variables if var.has_value]

        values = [var.value for var in assigned_vars]
        return len(values) == len(set(values))
    
