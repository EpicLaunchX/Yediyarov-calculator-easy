from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int

    def __post_init__(self):
        if not isinstance(self.first_operand, int) or not isinstance(self.second_operand, int):
            raise TypeError("Both operands must be integers")


# Define this function outside of the class
def operands_factory(first_operand: int, second_operand: int) -> Operands:
    if not isinstance(first_operand, int) or not isinstance(second_operand, int):
        raise TypeError("Both operands must be integers.")
    return Operands(first_operand, second_operand)
