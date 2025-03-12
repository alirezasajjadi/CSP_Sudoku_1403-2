from CSP.Constraint import Constraint
from CSP.Variable import Variable

class KillerCageConstraint(Constraint):
    """Ensures that variables in a cage have distinct values and sum to a target."""
    def __init__(self, variables: list[Variable], target_sum: int):
        super().__init__(variables)
        self.target_sum = target_sum

    def is_satisfied(self) -> bool:
        # Get assigned variables and their values
        assigned_vars = [var for var in self.variables if var.has_value]
        values = [var.value for var in assigned_vars]

        # Check for duplicates among assigned values
        if len(values) != len(set(values)):
            return False  # Duplicates found

        # If all variables are assigned, check the sum
        if len(assigned_vars) == len(self.variables):
            return sum(values) == self.target_sum

        # For partial assignments, ensure no duplicates (sum checked when complete)
        return True