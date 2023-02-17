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

    # @staticmethod
    # def _is_float(val):
    #     try:
    #         float(val)
    #         return True
    #     except:
    #         return False

    # @staticmethod
    # def _is_int(val):
    #     try:
    #         int(val)
    #         return True
    #     except:
    #         return False

    @staticmethod
    def _as_number(val):
        try:
            return Decimal(val)
        # if MyCalc._is_float(val):
        #     return Decimal(val)
        # elif MyCalc._is_int(val):
        #     return int(val)
        # else:
        except:
            raise Exception('Not a number.')

    # nn379 17 Feb 2023
    # Calc function to add, subtract, multiply and divide two numbers entered by the user
    def calc(self, num1, op, num2):
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
                        elif op in userInput and not handled:
                            nums = userInput.split(op)
                            handled = True

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