import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine, Patty, Topping, STAGE
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException, NeedsCleaningException
#this is an example test showing how to cascade fixtures to build up state
import random

class Test_BurgerMachine:
    
    # nn379 Mar 3 2023
    @pytest.fixture
    def machine(self):
        return BurgerMachine()

    # Setup a burger order as per the items sent in 'order_req'
    @pytest.fixture
    def setup_order(self):
        def _setup_order(order, order_req):
            order.handle_bun(order_req['bun'])
            [order.handle_patty(patty) for patty in order_req['patties']]
            [order.handle_toppings(topping) for topping in order_req['toppings']]
        return _setup_order

    # Create and pay for a burger order with the items sent in 'order_req', if no req is passed, use random items
    @pytest.fixture
    def normal_order(self, setup_order, machine):
        def _normal_order(machine = machine, req = {
            'bun': random.choice(machine.buns).name,
            'patties': [random.choice(machine.patties).name, 'next'],
            'toppings': [random.choice(machine.toppings).name, 'done']
        }):
            setup_order(machine, req)
            cost = machine.calculate_cost()
            machine.handle_pay(cost, cost)
            return machine, cost
        return _normal_order

    # Check for invalid stage by forcing the machine to handle patty when the stage is at the bun stage
    def test_bun_first(self, machine):
        with pytest.raises(InvalidStageException):
            machine.handle_patty("turkey")

        with pytest.raises(InvalidStageException):
            machine.handle_toppings("cheese")

    # Check whether the machine detects when the patties are out of stock by
    # 1. Decreasing the quantity of the patty to be tested to 2 instead of 10 for easier testing
    # 2. Creating an order with 3 of those patties to trigger the out of stock exception
    # 3. Asserting that exception message shows the correct patty name
    def test_patties_in_stock(self, machine, normal_order):
        req = {
            'bun': 'lettuce wrap',
            'patties': ['turkey', 'turkey', 'turkey', 'next']
        }
        machine.patties[0].quantity = 2
        with pytest.raises(OutOfStockException) as e:
            normal_order(req=req)
        assert str(e.value) == "Turkey patty is out of stock"

    # Check whether the machine detects when the toppings are out of stock by
    # 1. Decreasing the quantity of the topping to be tested to 2 instead of 10 for easier testing
    # 2. Creating an order with 3 of those toppings to trigger the out of stock exception
    # 3. Asserting that exception message shows the correct topping name
    def test_toppings_in_stock(self, machine, normal_order):
        req = {
            'bun': 'wheat burger bun',
            'patties': ['beef', 'next'],
            'toppings': ['cheese', 'cheese', 'cheese', 'done']
        }
        machine.toppings[3].quantity = 2
        with pytest.raises(OutOfStockException) as e:
            normal_order(req=req)
        assert str(e.value) == "Cheese topping is out of stock"

    # nn379 Mar 4 2023
    # 1. Check if the user can enter 3 patties of any type by passing random patties
    # 2. Verify that 3 elements of Patty type exist in inprogress_burger
    def test_three_patties(self, machine):
        machine.handle_bun('no bun')
        [machine.handle_patty(random.choice(machine.patties).name) for _ in range(3)]
        assert sum(isinstance(x, Patty) for x in machine.inprogress_burger) == 3

    # 1. Check if the user can enter 3 toppings of any type by passing random toppings
    # 2. Verify that 3 elements of Topping type exist in inprogress_burger
    def test_three_toppings(self, machine):
        machine.handle_bun('no bun')
        machine.handle_patty('beef')
        machine.handle_patty("next")
        [machine.handle_toppings(random.choice(machine.toppings).name) for _ in range(3)]
        assert sum(isinstance(x, Topping) for x in machine.inprogress_burger) == 3

    # 1. Create 3 burger orders and construct a req along with the total cost of the 3 orders
    # 2. Check whether the cost calculated by the machine is the same as the expected value of the orders
    def test_calculate_cost(self, machine, setup_order):
        bun1, bun2, bun3 = random.choice(machine.buns), random.choice(machine.buns), random.choice(machine.buns)
        patty1, patty2, patty3 = random.choice(machine.patties),random.choice(machine.patties), random.choice(machine.patties)
        topping1, topping2, topping3 = random.choice(machine.toppings), random.choice(machine.toppings), random.choice(machine.toppings)
        req = {
            'burger1': {
                'bun': bun1.name,
                'patties': [patty1.name, 'next'],
                'toppings': [topping1.name, 'done'],
                'cost': sum(i.cost for i in [bun1, patty1, topping1])
            },
            'burger2': {
                'bun': bun2.name,
                'patties': [patty2.name, 'next'],
                'toppings': [topping2.name, 'done'],
                'cost': sum(i.cost for i in [bun2, patty2, topping2])
            },
            'burger3': {
                'bun': bun3.name,
                'patties': [patty3.name, 'next'],
                'toppings': [topping3.name, 'done'],
                'cost': sum(i.cost for i in [bun3, patty3, topping3])
            }
        }
        for i in range(3):
            setup_order(machine, req[f'burger{i + 1}'])
            cost = machine.calculate_cost()
            assert cost == req[f'burger{i + 1}']['cost']
            machine.reset()
            
    # 1. Complete 3 orders and calculate their total cost
    # 2. Verify that the total cost matches the total sales completed by the machine 
    def test_total_sales(self, normal_order):
        first_order, cost1 = normal_order()
        second_order, cost2 = normal_order(first_order)
        third_order, cost3 = normal_order(second_order)
        total_cost = sum([cost1, cost2, cost3])
        assert third_order.total_sales == total_cost

    # Complete 4 burger orders and verify that the machine has sold a total of 4 burgers 
    def test_total_burgers(self, normal_order):
        first_order = normal_order()[0]
        second_order = normal_order(first_order)[0]
        third_order = normal_order(second_order)[0]
        normal_order(third_order)[0]
        assert third_order.total_burgers == 4

    # nn379 Mar 4 2023
    # 1. Reduce the remaining uses for the machine to 2
    # 2. Create a burger order which has 3 patties to trigger the NeedsCleaningException
    # 3. Clean the machine and verify that the remaning uses has been increased to 15
    def test_cleaning(self, machine):
        machine.remaining_uses = 2
        machine.handle_bun('wheat burger bun')
        with pytest.raises(NeedsCleaningException):
            [machine.handle_patty('beef') for _ in range(3)]
        machine.clean_machine()
        assert machine.remaining_uses == 15

    # Verify that the ExceededRemainingChoicesException works by attempting to add 4 patties of the same type to the machine
    def test_exceeded_choices(self, machine):
        machine.handle_bun('white burger bun')
        with pytest.raises(ExceededRemainingChoicesException):
            [machine.handle_patty('beef') for _ in range(4)]
        
    # Verify that InvalidChoiceException works by forcefully passing incorrect values to the buns / patties / toppings
    def test_invalid_choice(self, machine):
        with pytest.raises(InvalidChoiceException) as e:
            machine.handle_bun('lettuce')
        assert str(e.value) == "lettuce is not a valid choice of bun"
        machine.handle_bun('no bun')
        with pytest.raises(InvalidChoiceException) as e:
            machine.handle_patty('bun')
        assert str(e.value) == "bun is not a valid choice of patty"