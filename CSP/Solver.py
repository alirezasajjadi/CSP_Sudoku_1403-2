import os
import subprocess
import time
from collections import deque
from copy import deepcopy
from typing import Optional

from CSP.Problem import Problem
from CSP.Variable import Variable


class Solver:

    def __init__(self, problem: Problem):
        """
        Initializes the Solver object with the given problem instance and optional parameters.

        Args:
            problem (Problem): The problem instance to be solved.
        """
        self.problem = problem
        self.back_up = deque()

    def is_finished(self) -> bool:
        """
        Determines if the problem has been solved.

        Returns:
            bool: True if the problem has been solved, False otherwise.
        """
        return all([x.is_satisfied() for x in self.problem.constraints]) and len(
            self.problem.get_unassigned_variables()) == 0

    def solve(self):
        """
        Solves the problem instance using the backtracking algorithm with optional heuristics.
        """
        start = time.time()
        result = self.backtracking()
        end = time.time()
        time_elapsed = (end - start) * 1000
        if result:
            print(f'Solved after {time_elapsed} ms')
        else:
            print(f'Failed to solve after {time_elapsed} ms')

    def backtracking(self) -> bool:
        """
        Implements the backtracking algorithm.

        Returns:
            bool: True if the problem has been solved, False otherwise.
        """
        if self.is_finished():
            return True
        var = self.mrv()
        ordered_values = self.lcv(var)  
        for value in ordered_values:
            self.save_domain(self.problem.variables)
            var.value = value
            if self.is_consistent(var) and self.forward_check(var): 
                result = self.backtracking()
                if result:
                    return True
            var.value = None
            self.load_domain(self.problem) 
        return False

    def forward_check(self, var: Variable) -> bool:
        """
        Implements the Forward Checking algorithm.

        """
        constraints = self.problem.get_constraints(var)

        for neighbor in var.neighbors:
            if neighbor.has_value:
                continue
            tmp = neighbor.domain.copy()
            for value in tmp:
                neighbor.value = value
                for constraint in constraints:
                    if neighbor in constraint.variables:
                        if not constraint.is_satisfied():
                            tmp.remove(value)
                            break                
            neighbor.value = None
            if len(tmp) == 0:
                return False
            else:
                neighbor.domain=tmp              
        return True
                        

    def mrv(self) -> Optional[Variable]:
        """
        Implements the Minimum Remaining Values heuristic.

        Returns:
            Optional[Variable]: The variable with the smallest domain or None if all variables have been assigned.
        """
        unassigned = self.problem.get_unassigned_variables()
        if not unassigned:
            return None
        mrv = unassigned[0]
        for var in unassigned:
            if len(var.domain) < len(mrv.domain):
                mrv = var
        return mrv      

    def is_consistent(self, var: Variable) -> bool:
        """
        Determines ifthe given variable is consistent with all constraints.

        Args:
            var (Variable): The variable to be checked for consistency.

        Returns:
            bool: True if the variable is consistent with all constraints, False otherwise.
        """
        return all(constraint.is_satisfied() for constraint in self.problem.constraints if var in constraint.variables)

    def lcv(self, var: Variable):
        """
        Implements the Least Constraining Values heuristic.

        Args:
            var (Variable): The variable whose domain values are to be ordered.

        Returns:
            List: The domain values of the variable ordered according to the number of conflicts they cause.
        """
        domain_values = var.domain
        constraints = self.problem.get_constraints(var)
        conflicts_count = {}
        for value in domain_values:
            var.value = value
            conflicts_count[value] = 0
            for constraint in constraints:
                if not constraint.is_satisfied():
                    conflicts_count[value] += 1
            var.value = None
        ordered_values = sorted(domain_values, key=lambda value: conflicts_count[value])
        return ordered_values
    
    def save_domain(self, vars: list[Variable]):
        self.back_up.append([var.domain.copy() for var in vars])
    
    def load_domain(self, problem: Problem):
        domains = self.back_up.pop()
        for i in range(len(problem.variables)):
            problem.variables[i].domain = domains[i]
