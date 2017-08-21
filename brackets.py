#!/usr/bin/env python
"""This module contains util for work with brackets expressions.
This util is implemented in class BracketExpression.
Use this class to create and validate brackets expresiions.
"""
import sys


class BracketExpression:
    """Class BracketExpression is used to check
    balance of brackets in any expression.
    Actually, instance of class BracketExpression is simple string
    with util method isValid() which checks balance of brackets in it.
    """

    __opened = ["(", "[", "{", "<"]
    __closed = [")", "]", "}", ">"]
    __bracketsMap = {}
    __isExpressionValid = None

    def __init__(self, value):
        """Construnctor takes one argument.
        This value is to be validated.
        """
        self.__value = str(value)

    def getValue(self):
        """Getter method returns initial value.
        """
        return self.__value

    def isValid(self):
        """Method isValid doesn't take any arguments.
        It uses stack principe to check brackets balance.
        """

        # If expression is already validated, just return result.
        if self.__isExpressionValid is not None:
            return self.__isExpressionValid

        # Lazy preparing of brackets map for case when
        # isValid() is not called for expression.
        if not self.__bracketsMap:
            self.__bracketsMap = dict(zip(self.__opened, self.__closed))

        # Empty stack.
        bracketsStack = []

        # Check every symbol of initial expression
        for letter in self.__value:
            # If symbol is opened bracket, push it to stack.
            if letter in self.__opened:
                bracketsStack.append(letter)
            # If symbol is closed bracket, validate it.
            # Otherwise, it's any symbol, it could be skipped in this version.
            elif letter in self.__closed:
                try:
                    # Pop the latest opened brackets from stack.
                    bracket = bracketsStack.pop()
                except:
                    # If stack is empty, there is no opened bracket
                    # for this closed bracket.
                    # All opened brackets are closed. Expression is not valid.
                    self.__isExpressionValid = False
                    return self.__isExpressionValid
                else:
                    # If the latest opened brackets doesn't correspond
                    # to this closed bracket, expression is not valid.
                    # Otherwise, continue to check.
                    if not self.__bracketsMap[bracket] == letter:
                        self.__isExpressionValid = False
                        return self.__isExpressionValid

        # If stack is not empty, there are opened bracked which are not closed,
        # expression is not valid.
        # Otherwise, all brackets are closed. Expression is valid.
        if bracketsStack:
            self.__isExpressionValid = False
        else:
            self.__isExpressionValid = True

        return self.__isExpressionValid


if __name__ == "__main__":
    # Call script from shell with argument in quotes like:
    # python brackets.py ""
    # Empty string is valid expression.
    try:
        expression = BracketExpression(sys.argv[1])
        print(expression.getValue())
        print(expression.isValid())
    except IndexError:
        raise Exception('No value')
