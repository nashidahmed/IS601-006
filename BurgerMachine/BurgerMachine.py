from enum import Enum
import sys
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException
from BurgerMachineExceptions import InvalidPaymentException

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity = 10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    # nn379 Mar 2 2023
    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            # Raise an exception and inform the user that the item they chose is out of stock in the category
            raise OutOfStockException(f'{self} {self.__class__.__name__.lower()} is out of stock')
        return self.quantity 

    def in_stock(self):
        return self.quantity > 0
    def __repr__(self) -> str:
        return self.name

class Bun(Usable):
    pass

class Patty(Usable):
    pass

class Topping(Usable):
    pass

class STAGE(Enum):
    Bun = 1
    Patty = 2
    Toppings = 3
    Pay = 4

class BurgerMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 15
    MAX_PATTIES = 3
    MAX_TOPPINGS = 3

    def __init__(self):
        self.buns = [Bun(name="No Bun", cost=0), Bun(name="White Burger Bun", cost=1), Bun("Wheat Burger Bun", cost=1.25),Bun("Lettuce Wrap", cost=1.5)]
        self.patties = [Patty(name="Turkey", quantity=10, cost=1), Patty(name="Veggie", quantity=10, cost=1), Patty(name="Beef", quantity=10, cost=1)]
        self.toppings = [Topping(name="Lettuce", quantity=10, cost=.25), Topping(name="Tomato", quantity=10, cost=.25), Topping(name="Pickles", quantity=10, cost=.25), \
        Topping(name="Cheese", quantity=10, cost=.25), Topping(name="Ketchup", quantity=10, cost=.25),
        Topping(name="Mayo", quantity=10, cost=.25), Topping(name="Mustard", quantity=10, cost=.25),Topping(name="BBQ", quantity=10, cost=.25)] 

        # variables
        self.remaining_uses = self.USES_UNTIL_CLEANING
        self.remaining_patties = self.MAX_PATTIES
        self.remaining_toppings = self.MAX_TOPPINGS
        self.total_sales = 0
        self.total_burgers = 0

        self.inprogress_burger = []
        self.currently_selecting = STAGE.Bun

    # rules
    # 1 - bun must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - patties can't exceed max
    # 4 - toppings can't exceed max
    # 5 - proper cost must be calculated and shown to the user
    # 6 - cleaning must be done after certain number of uses before any more burgers can be made
    # 7 - total sales should calculate properly based on cost calculation
    # 8 - total_burgers should increment properly after a payment
    

    def pick_bun(self, choice):
        if self.currently_selecting != STAGE.Bun:
            raise InvalidStageException
        for c in self.buns:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_burger.append(c)
                return
        # nn379 Mar 2 2023
        # Inform the user that the item they entered does not exist in the category
        raise InvalidChoiceException(f'{choice} is not a valid choice of {self.currently_selecting.name.lower()}')

    def pick_patty(self, choice):
        if self.currently_selecting != STAGE.Patty:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_patties <= 0:
            raise ExceededRemainingChoicesException
        for f in self.patties:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_burger.append(f)
                self.remaining_patties -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException(f'{choice} is not a valid choice of {self.currently_selecting.name.lower()}')

    def pick_toppings(self, choice):
        if self.currently_selecting != STAGE.Toppings:
            raise InvalidStageException
        if self.remaining_toppings <= 0:
            raise ExceededRemainingChoicesException
        for t in self.toppings:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_burger.append(t)
                self.remaining_toppings -= 1
                return
        raise InvalidChoiceException(f'{choice} is not a valid choice of {self.currently_selecting.name.lower()}')

    def reset(self):
        self.remaining_patties = self.MAX_PATTIES
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_burger = []
        self.currently_selecting = STAGE.Bun

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        
    def handle_bun(self, bun):
        self.pick_bun(bun)
        self.currently_selecting = STAGE.Patty

    def handle_patty(self, patty):
        if patty == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_patty(patty)

    def handle_toppings(self, toppings):
        if toppings == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_toppings(toppings)

    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        try:
            if float(total) == expected:
                print("Thank you! Enjoy your burger!")
                self.total_burgers += 1
                self.total_sales += expected
                print(f"Total sales so far ${self.total_sales:.2f}")
                self.reset()
            else:
                raise InvalidPaymentException
        except:
            raise InvalidPaymentException
        
    def print_current_burger(self):
        print(f"Current Burger: {','.join([x.name for x in self.inprogress_burger])}")

    # nn379 Mar 2 2023
    # Compute the sum by creating an array of costs from the inprogress_burger list and adding them with sum
    def calculate_cost(self):
        return sum([item.cost for item in self.inprogress_burger])

    def run(self):
        try:
            if self.currently_selecting == STAGE.Bun:
                bun = input(f"What type of bun would you like {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.buns))))}?\n")
                self.handle_bun(bun)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Patty:
                patty = input(f"What type of patty would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.patties))))}? Or type next.\n")
                self.handle_patty(patty)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Toppings:
                toppings = input(f"What topping would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
                self.handle_toppings(toppings)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Pay:
                # nn379 Mar 2 2023
                expected = self.calculate_cost()
                # Use string formatting to display the expected value in currency format
                total = input(f"Your total is ${expected:.2f}, please enter the exact value.\n$")
                self.handle_pay(expected, total.strip())
                
                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    #exit() in recursive functions creates stackoverflow
                    # use return 1 to exit
                    print("Quitting the burger machine")
                    return 1
        except KeyboardInterrupt:
            # quit
            print("Quitting the burger machine")
            sys.exit()
        # nn379 Mar 2 2023
        except OutOfStockException as e:
            # Print the exception message from the OutOfStockException
            print(e)
        except NeedsCleaningException:
            # The while loop asks the user to type 'clean' to clean the machine.
            # 1. If any other input is entered, the user is informed that the machine was not cleaned and asked to type again.
            # 2. When the user types clean, clean_machine is called and the user is informed that the machine has been cleaned
            while(input("The burger machine needs cleaning. Type 'clean' to clean the machine\n") != 'clean'):
                print('The machine was not cleaned')
            else:
                self.clean_machine()
                print('The machine was cleaned')
        except InvalidChoiceException as e:
            # Print the exception message from the InvalidChoiceException
            print(e)
        except ExceededRemainingChoicesException:
            # Inform the user that they cannot add any more items in that category and the force stage to move to the next category.
            print(f'You cannot add any more {self.currently_selecting.name.lower()}')
            self.currently_selecting = STAGE(self.currently_selecting.value + 1)
        except InvalidPaymentException:
            # Inform the user that they have entered an incorrect amount
            print('You have entered an incorrect amount')
        except:
            print("Something went wrong")
        
        self.run()

    def start(self):
        self.run()

    
if __name__ == "__main__":
    bm = BurgerMachine()
    bm.start()