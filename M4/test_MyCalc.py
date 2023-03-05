import pytest
from MyCalc import MyCalc
from decimal import Decimal

class Test_MyCalc:
    
    @pytest.fixture
    def my_calc(self):
        return MyCalc()
    
    # nn379 17 Feb 2023
    @pytest.fixture
    def data_number(self):
        """ Data inputs for different test cases along with their outputs for data without 'ans' input """
        return [{
            "operand1": "3",
            "operand2": "5",
            "resAdd": "8",
            "resSub": "-2",
            "resMul": "15",
            "resDiv": "0.6"
        }, {
            "operand1": "0.1",
            "operand2": "0.2",
            "resAdd": "0.3",
            "resSub": "-0.1",
            "resMul": "0.02",
            "resDiv": "0.5"
        }, {
            "operand1": "-6",
            "operand2": "-3",
            "resAdd": "-9",
            "resSub": "-3",
            "resMul": "18",
            "resDiv": "2"
        }, {
            "operand1": "are",
            "operand2": ".1",
            "negative": True,
        }]
    
    # nn379 17 Feb 2023
    @pytest.fixture
    def data_ans(self, my_calc):
        """ Data inputs for different test cases along with their outputs for data with 'ans' input """
        my_calc.ans = 5
        return [{
            "operand1": "ans",
            "operand2": "2",
            "resAdd": "7",
            "resSub": "3",
            "resMul": "10",
            "resDiv": "2.5"
        }, {
            "operand1": "2.1",
            "operand2": "ans",
            "resAdd": "9.1",
            "resSub": "-0.9",
            "resMul": "21",
            "resDiv": "0.84"
        }]
    
    # nn379 17 Feb 2023
    # Call the test helper function with the my_calc instance, data_number which is the data set for number strings and not 'ans', '+' and 'resAdd'
    def test_number_add_number(self, my_calc, data_number):
        test_helper(my_calc, data_number, '+', 'resAdd')
                
    # nn379 17 Feb 2023
    # Call the test helper function with the my_calc instance, data_ans which is the data set for number strings which may contain 'ans', '+' and 'resAdd'
    def test_ans_add_number(self, my_calc, data_ans):
        test_helper(my_calc, data_ans, '+', 'resAdd')

    # nn379 17 Feb 2023
    # Call the test helper function with the my_calc instance, data_number which is the data set for number strings and not 'ans', '-' and 'resSub'
    def test_number_sub_number(self, my_calc, data_number):
        # Add two test cases to the existing data set for the two cases where the first number or second number is negative
        data_number.extend([{
            "operand1": "-5",
            "operand2": "3",
            "resSub": "-8"
        }, {
            "operand1": "8",
            "operand2": "-3",
            "resSub": "11"
        }])
        test_helper(my_calc, data_number, '-', 'resSub')

    # nn379 17 Feb 2023
    # Call the test helper function with the my_calc instance, data_ans which is the data set for number strings which may contain 'ans', '-' and 'resSub'
    def test_ans_sub_number(self, my_calc, data_ans):
        test_helper(my_calc, data_ans, '-', 'resSub')

    # nn379 17 Feb 2023
    # Call the test helper function with the my_calc instance, data_number which is the data set for number strings and not 'ans', '*' or 'x' and 'resMul'
    def test_number_mul_number(self, my_calc, data_number):
        test_helper(my_calc, data_number, '*', 'resMul')

    # nn379 17 Feb 2023
    # Call the test helper function with the my_calc instance, data_ans which is the data set for number strings which may contain 'ans', '*' or 'x' and 'resMul'
    def test_ans_mul_number(self, my_calc, data_ans):
        test_helper(my_calc, data_ans, 'x', 'resMul')

    # nn379 17 Feb 2023
    # Call the test helper function with the my_calc instance, data_number which is the data set for number strings and not 'ans', '/' and 'resDiv'
    def test_number_div_number(self, my_calc, data_number):
        # Add the test case to check if exception is thrown when the user tries to divide by 0
        data_number.append({
            "operand1": "5",
            "operand2": "0",
            "negative": True,
            "zeroTest": True
        })
        test_helper(my_calc, data_number, '/', 'resDiv')

    # nn379 17 Feb 2023
    # Call the test helper function with the my_calc instance, data_ans which is the data set for number strings which may contain 'ans', '/' and 'resDiv'
    def test_ans_div_number(self, my_calc, data_ans):
        test_helper(my_calc, data_ans, '/', 'resDiv')

# nn379 17 Feb 2023
# This function takes in 4 parameters, namely:
# 1. 'my_calc' class instance which is obtained through a fixture.
# 2. 'data' which is obtained through a fixture
# 3. 'operation' which is passed in from the respective test cases as per what operation needs to be performed on the two numbers.
# 4. 'res' which is the name of the key in the data list of dictonaries for the result of the respective operation
# The function loops over the data and the following takes place:
# 1. If 'negative' does not exist in the dict, it is a positive test case, assert that the result of the calc() is as expected. Convert to Decimal since the calc() returns a Decimal
# 2. Else, if 'negative' exists in the dict, check if it is a ZeroDivisionError test case or not
# 3. If is not a ZeroDivisionError test case, check if the exception returned is not a number
# 4. Else, it is a ZeroDivisionError test case, so check if the exception returned is cannot divide by zero
@pytest.mark.skip(reason="test_helper is a helper function")
def test_helper(my_calc, data, operation, res):
    """ test helper function to test the calculator """
    for d in data:
        if 'negative' not in d:
            r = my_calc.calc(d['operand1'], operation, d['operand2'])
            assert r == Decimal(d[res]), "Normal addition"
        # Test failed test cases by checking for the exception thrown
        elif d['negative']:
            if 'zeroTest' not in d:
                with pytest.raises(Exception) as e:
                    my_calc.calc(d['operand1'], operation, d['operand2'])
                assert str(e.value) == "Not a number."
            # Test the case where the denominator is 0 in the divide case
            elif d['zeroTest']:
                with pytest.raises(ZeroDivisionError) as e:
                    my_calc.calc(d['operand1'], operation, d['operand2'])
                assert str(e.value) == "Cannot divide by zero."
