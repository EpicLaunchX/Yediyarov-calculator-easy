from src.pytemplate.domain.models import Operands


class Calculator:
    def add(self, operands: Operands):
        return operands.first_operand + operands.second_operand

    def subtract(self, operands: Operands):
        return operands.first_operand - operands.second_operand

    def multiply(self, operands: Operands):
        return operands.first_operand * operands.second_operand

    def divide(self, operands: Operands):
        if operands.second_operand == 0:
            raise ValueError("Cannot divide by zero")
        return operands.first_operand / operands.second_operand