import operator
from decimal import Decimal

class MyCalc:

    ans = 0

    operators = {
        '+': operator.add,
        '*': operator.mul,
        'x': operator.mul,
        '/': operator.truediv,
        '-': operator.sub
    }

    # nn379 17 Feb 2023
    # The number passed as a string is attempted to be converted into a number using the Decimal function, if it is not a number, an exception is thrown informing the user that the string is not a number
    @staticmethod
    def _as_number(val):
        """ method to check if the string passed is a number or not """
        try:
            return Decimal(val)
        except:
            raise Exception('Not a number.')

    # nn379 17 Feb 2023
    # Check if the any of the strings passed contains the value 'ans', if it does recursively call the function passing the values of the 'ans' as a string.
    # If the string do not contain 'ans' in them, then:
    # 1. Try to convert the strings to numbers. If unsuccessful, re-raise the exception raised by the _as_number function.
    # 2. If successful, use the operator passed to execute the expression on the two numbers and set the result to 'ans'
    # 3. If a ZeroDivisionError is thrown when division is performed with a denominator as 0, raise as exception informing the user that a number cannot be divided by 0
    # 4. If the no exceptions are thrown, return 'ans'.
    def calc(self, num1, op, num2):
        """ add, subtract, multiply and divide two numbers which are passed as strings. The operation to be done on the numbers is also passed in """
        if num1 == 'ans' or num2 == 'ans':
            return self.calc(str(self.ans), op, num2) if num1 == 'ans' else self.calc(num1, op, str(self.ans))
        else:
            try:
                num1 = self._as_number(num1)
                num2 = self._as_number(num2)
                self.ans = MyCalc.operators[op](num1, num2)
            except ZeroDivisionError:
                raise ZeroDivisionError('Cannot divide by zero.')
            except Exception:
                raise
        return self.ans

if __name__ == '__main__':
    isRunning = True
    calc = MyCalc()
    ops = [*calc.operators]
    userInput = input('Are you ready? ')
    if userInput == 'yes' or userInput == 'y':
        while isRunning:
            userInput = input('What do you want to calculate? ')
            if userInput == 'quit' or userInput == 'q':
                isRunning = False
            else:
                handled = False
                for op in ops:
                    try:
                        nums = []
                        # nn379 17 Feb 2023
                        # Check if operation is '-', if so, handle a special case since numbers can also be negative:
                        # 1. Count number of '-' in the user entered string
                        # 2. If there are three '-'s, eg. '-3 - -4', or two '-'s where the first number is negative eg. '-3 - 4', split from second '-' and assign the value after the split to num2 (-4, 4 respectively) and join the first number with '-' to get num1 (-3)
                        # 3. Else if second number is negative or both are positive, simply split over the first '-'
                        # 4. Assign both values to num array to calculate and print later
                        if op == '-' and not handled:
                            num_minus = userInput.count(op)
                            if num_minus == 3 or (num_minus == 2 and userInput.strip()[0] == op):
                                num1 = op.join(userInput.split(op, 2)[:2])
                                num2 = userInput.split(op, 2)[2]
                                nums = [num1, num2]
                            else:
                                num1 = userInput.split(op, 1)[0]
                                num2 = userInput.split(op, 1)[1]
                                nums = [num1, num2]
                        # If op is not '-', simply split over the op
                        elif op in userInput and not handled:
                            nums = userInput.split(op)

                        # If nums was filled with 2 variables from the operation above, call the calc() and print the output 
                        if len(nums) == 2:
                            res = calc.calc(nums[0].replace(' ', ''), op, nums[1].replace(' ', ''))
                            print(nums[0].replace(' ', ''), op, nums[1].replace(' ', ''), '=', res)
                            handled = True
                    except Exception as e:
                        print(e)
                if not handled:
                    print("Action not supported. Please try again.")
    else:
        print('Goodbye')