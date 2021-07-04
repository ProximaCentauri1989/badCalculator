class OperatorError(Exception):
    """Exception raised for invalid operators.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, val, message="Invalid operator"):
        self.message = message
        self.val = val
        super().__init__(self.message)

class OperandError(Exception):
    """Exception raised for invalid operands.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, val, message="Invalid operand"):
        self.message = message
        self.val = val
        super().__init__(self.message)
