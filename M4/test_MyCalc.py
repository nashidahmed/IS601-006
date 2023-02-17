import pytest
from MyCalc import MyCalc
from decimal import Decimal

class Test_MyCalc:
    
    @pytest.fixture
    def my_calc(self):
        return MyCalc()
    
    @pytest.fixture
    def data_number(self):
        # Data inputs for different test cases along with their outputs
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
    
    @pytest.fixture
    def data_ans(self, my_calc):
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
    
    

    def test_number_add_number(self, my_calc, data_number):
        test_helper(my_calc, data_number, '+', 'resAdd')
                
    def test_ans_add_number(self, my_calc, data_ans):
        test_helper(my_calc, data_ans, '+', 'resAdd')

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

    def test_ans_sub_number(self, my_calc, data_ans):
        test_helper(my_calc, data_ans, '-', 'resSub')

    def test_number_mul_number(self, my_calc, data_number):
        test_helper(my_calc, data_number, '*', 'resMul')


    def test_ans_mul_number(self, my_calc, data_ans):
        test_helper(my_calc, data_ans, 'x', 'resMul')

    def test_number_div_number(self, my_calc, data_number):
        # Add the test case to check what happens when the user tries to divide by 0
        data_number.append({
            "operand1": "5",
            "operand2": "0",
            "negative": True,
            "zeroTest": True
        })
        test_helper(my_calc, data_number, '/', 'resDiv')

    def test_ans_div_number(self, my_calc, data_ans):
        test_helper(my_calc, data_ans, '/', 'resDiv')

# Test helper function to test the calculator
def test_helper(my_calc, data, operation, res):
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
