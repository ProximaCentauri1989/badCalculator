import sys
from utils import *
from exceptions import *

EXPECTED_OPERATORS = "+-*/"

"""
prepareExpression function expects right logical sequence in an expression
Every expression starts from some operand followed by an operators which is followed be next operand, etc.
"""
def prepareExpression(expression):
    operands = []
    operators = []

    exp = expression.split(sep = ' ')
    for index, val in enumerate(exp):
        if not index % 2:
            operands.append(val)
        else:
            operators.append(val)

    return operands, operators

def calculateExpression(operands, operators):
    if not operands:
        raise Exception("Invalid expression provided. No operands to calculate expression")
    if not operators:
        raise Exception("Invalid expression provided. No operators to calculate expression")

    # take first operand as a result. Then in the correct expression a length of both arrays, operands and operators, should be the same
    res = getOperand(operands[0])

    operands = operands[1:]
    for index, val in enumerate(operands):
        if not isValidOperator(operators[index], EXPECTED_OPERATORS):
            raise OperatorError(operators[index])

        val = getOperand(operands[index])

        if operators[index] == "+":
            res += val
        elif operators[index] == "-":
            res -= val
        elif operators[index] == "*":
            res *= val
        else:
            if not val:
                raise ZeroDivisionError()
            res /= val

    return res


"""
Bad calculator which doesn't care about priorities
"""

def main():
    if len(sys.argv) == 1:
        print("No expression provided")
        return

    expression = sys.argv[1]
    [operands, operators] = prepareExpression(expression)

    try:
        res = calculateExpression(operands, operators)
    except OperatorError as err:
        print("Invalid expression provided: {}". format("{} {}".format(err.message, err.val)))
    except OperandError as err:
        print("Invalid expression provided: {}". format("{} '{}'".format(err.message, err.val)))
    except ZeroDivisionError:
        print("Invalid expression provided. Division be zero")
    except Exception as err:
        print(err)
    else:
        print("Result is: {}".format(res))

if (__name__ == '__main__'):
    main()
