"""
Develop an automated code review system that analyzes
Python code and provides feedback on code quality, potential errors,
and adherence to coding standards. Use AI to generate
the code that performs this analysis and review the code itself for potential issues.
"""

import ast
import re


class CodeAnalyzer:
    """
    Analyzes Python code to detect potential issues like unused imports,
    missing docstrings, and other code quality issues.
    """
    def __init__(self, code):
        self.code = code
        self.tree = ast.parse(code)

    def detect_unused_imports(self):
        """
        Detects unused imports in the Python code.
        
        Returns:
            list: A list of unused imports found in the code.
        """
        imported_names = set()
        used_names = set()

        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_names.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    imported_names.add(alias.name)
            elif isinstance(node, ast.Name):
                used_names.add(node.id)

        unused_imports = imported_names - used_names
        return list(unused_imports)

    def detect_missing_docstrings(self):
        """
        Detects functions or methods missing docstrings.
        
        Returns:
            list: A list of function names that are missing docstrings.
        """
        missing_docstrings = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                if ast.get_docstring(node) is None:
                    missing_docstrings.append(node.name)
        return missing_docstrings

    def check_variable_redefinitions(self):
        """
        Detects cases where variables are redefined in the same scope.
        
        Returns:
            list: A list of variable names that are redefined.
        """
        variable_assignments = set()
        redefined_variables = set()

        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        if target.id in variable_assignments:
                            redefined_variables.add(target.id)
                        variable_assignments.add(target.id)

        return list(redefined_variables)

    def check_pep8(self):
        """
        Checks for potential PEP 8 violations in the code.
        
        Returns:
            list: A list of potential PEP 8 violations found in the code.
        """
        violations = []

        # Check for lines exceeding 79 characters
        lines = self.code.split("\n")
        for i, line in enumerate(lines):
            if len(line) > 79:
                violations.append(f"Line {i + 1}: Exceeds 79 characters")

        # Check for missing whitespace around operators
        operator_patterns = r"(?<=\S)([+\-*/%&|^=<>!])(?=\S)"
        for i, line in enumerate(lines):
            if re.search(operator_patterns, line):
                violations.append(f"Line {i + 1}: Missing space around operators.")

        return violations

    def analyze(self):
        """
        Analyzes the code and returns a dictionary with various analysis results.
        
        Returns:
            dict: A dictionary containing results of the analysis.
        """
        return {
            "unused_imports": self.detect_unused_imports(),
            "missing_docstrings": self.detect_missing_docstrings(),
            "redefined_variables": self.check_variable_redefinitions(),
            "pep8_violations": self.check_pep8(),
        }


class ReportGenerator:
    """
    Generates a code review report based on the analysis of the code.
    """
    def __init__(self, code):
        self.code = code
        self.analyzer = CodeAnalyzer(code)

    def generate_report(self):
        """
        Generates a detailed report on the code quality, potential errors,
        and adherence to coding standards.

        Returns:
            str: The generated report in a human-readable format.
        """
        analysis = self.analyzer.analyze()
        report = "Code Review Report\n"
        report += "=" * 30 + "\n"
        issues_detected = False

        # Unused Imports
        if analysis["unused_imports"]:
            issues_detected = True
            report += "Issues Detected:\n"
            for imp in analysis["unused_imports"]:
                report += f"1. Unused import: '{imp}'\n"
                report += "   - Recommendation: Remove unused imports to improve code clarity.\n"

        # Missing Docstrings
        if analysis["missing_docstrings"]:
            issues_detected = True
            for func in analysis["missing_docstrings"]:
                report += f"2. Missing docstring for function: '{func}'\n"
                report += "   - Recommendation: Add a docstring to explain the function's purpose.\n"

        # Redefined Variables
        if analysis["redefined_variables"]:
            issues_detected = True
            for var in analysis["redefined_variables"]:
                report += f"3. Variable redefined: '{var}'\n"
                report += "   - Recommendation: Avoid redefining variables in the same scope to maintain clarity.\n"

        # PEP 8 Violations
        if analysis["pep8_violations"]:
            issues_detected = True
            for violation in analysis["pep8_violations"]:
                report += f"4. PEP 8 violation: {violation}\n"
                report += "   - Recommendation: Follow PEP 8 guidelines to improve code readability and maintainability.\n"

        if not issues_detected:
            report += "No issues detected. Code follows best practices.\n"
        return report


if __name__ == "__main__":
    print("Automated Code Review")

    code = """
import math
import os
from datetime import datetime
from collections import defaultdict

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return math.pi * radius ** 2

def get_current_time():
    return datetime.now()
    """

    report_generator = ReportGenerator(code)
    print(report_generator.generate_report())
