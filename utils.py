from exceptions import *

def isInteger(obj):
    try:
        int(obj)
        return True
    except ValueError:
        return False

def isFloat(obj):
    try:
        float(obj)
        return True
    except ValueError:
        return False

def isValidOperator(operator, expectedOperators):
    return operator in expectedOperators

def getOperand(operand):
    if isInteger(operand):
        return int(operand)
    elif isFloat(operand):
        return float(operand)
    else:
        raise OperandError(operand)
