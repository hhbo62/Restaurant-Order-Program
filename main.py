#Link: https://github.com/hhbo62/Restaurant-Order-Program
#Add: openFiles.py (after finished) Add: acurate totals.
#note: this is the main program. All other files are test files (except stats.txt).
from time import sleep

#Version
version = 2.5

about_screen = f"""
\tThis is Resturaunt Order Program v.{version}
\tMade by me (obviously)

\n\tVersion {version} is here!
\tAdded:
\t\t(MAJOR) More efficient program code using classes
\t\tWebpage
\n\tComing Soon:\n
\t\tHelp page
\t\tA GUI
"""
quantity = 00

#Class
class FoodsList():
    def __init__(self):
        self.items = []
        self.quantity = 0
        self.totalPrice = 0
        self.totalCal = 0

    def addFood(self, foodObject):
        self.items.append(foodObject)


    def getTotalPrice(self):
        self.totalPrice = 0
        for item in self.items:
            item.getPrice()
            self.totalPrice += int(item.totalPrice)

    def getTotalCal(self):
        self.totalCal = 0
        for item in self.items:
            item.getCal()
            self.totalCal += int(item.cal)


class Food():
    def __init__(self, food, qt, price, cal):
        self.food = food
        self.qt = qt
        self.price = price
        self.cal = cal


    def getPrice(self):
        self.totalPrice = int(self.price) * self.qt

    def getQt(self):
        self.quantity = self.qt

    def getCal(self):
        self.cal = self.cal


#Confirm
def confirm():
    print('\n\tConfirm? (0=No/1=Yes)')
    confirm_var = input()

    if confirm_var == "1":
        print("\nPosting Order...")
        sleep(2.5)
        print("Order Posted")
        print("Exiting Program")
        sleep(1)
    elif confirm_var == "0":
        print("Restarting Order...\n")
        run_program()

    else:
        print("Please enter a valid value")
        confirm()


#proccess
def take_order():
    #Taking it
    print(
        f'Sandwich: (300 calories, $2.00)'
    )
    sandwich_answer1 = input()
    sandwhich = Food("sandwhich", sandwich_answer1, 2.00, 300)
    foodslist.addFood(sandwhich)


    print(
        f'\nPancake: (300 calories, $2.00)'
    )
    pancake_answer1 = input()
    pancake = Food("pancake", pancake_answer1, 2.00, 300)
    foodslist.addFood(pancake)

    print(
        f'\nScrambled Eggs: (300 calories, $2.00)'
    )
    se_answer1 = input()
    se = Food("se", se_answer1, 2.00, 300)
    foodslist.addFood(se)

    print(
        f'\nBoiled Eggs: (300 calories, $2.00)'
    )
    be_answer1 = input()
    be = Food("be", be_answer1, 2.00, 300)
    foodslist.addFood(be)

    print(
        f'\nBreakfast Pizza: (300 calories, $2.00)'
    )
    bp_answer1 = input()
    bp = Food("bp", bp_answer1, 2.00, 300)
    foodslist.addFood(bp)

    print(f' \n\tYour Order:\n')

    #to display or not to display. That is the question
    sandwhich.getQt()
    if int(sandwhich.quantity) > 0:
        if int(sandwhich.quantity) == 1:
            print("One Sandwich")
        else:
            print(f'Sandwiches: {sandwhich.quantity}')

    pancake.getQt()
    if float(pancake.quantity) > 0:
        if float(pancake.quantity) == 1:
            print("One Pancake")
        else:
            print(f'Pancakes: {pancake.quantity}')

    se.getQt()
    if float(se.quantity) > 0:
        if float(se.quantity) == 1:
            print("One Scrambled Egg")
        else:
            print(f'Scrambled Eggs: {se.quantity}')

    be.getQt()
    if float(be.quantity) > 0:
        if float(be.quantity) == 1:
            print("One Boiled Egg")
        else:
            print(f'Boiled Eggs: {be.quantity}')

    bp.getQt()
    if float(bp.quantity) > 0:
        if float(bp.quantity) == 1:
            print("One Breakfast Pizza")
        else:
            print(f'Breakfast Pizzas: {bp.quantity}')
    #total price+Cal
    foodslist.getTotalPrice()

    print("Total Price:")
    print(f'${foodslist.totalPrice}')

    foodslist.getTotalCal()
    print("Total Cals:")
    print(foodslist.totalCal)

#run
def run_program():
    print("\n\tResturant Order Form:")
    take_order()
    confirm()


#ask
def ask():
    print("\n\tWelcome to Resturaunt Order Program!")
    start_about_help = input(
        f'\n\nWebsite: https://hhbo62.github.io/Restaurant-Order-Program/\nThis is version {version}.\n\nType [start] to start program. \nType[About] to go to the about screen (and see what changed in the new update). \nType [help] to go to help. \nType [exit] to exit program. '
    )

    answer = start_about_help.lower()
    start(answer)


#main running of program
def start(answer):

    if answer == "start":
        run_program()
        run_again = input(
            "Type [run] to run again type [exit] to stop program ")
        if run_again.lower() == "run":
            run_program()
        elif run_again.lower() == "exit":
            print("bye!")
    elif answer == "about":
        print(about_screen)
        exit_about = input("type [exit] to exit ")
        if exit_about.lower() == "exit":
            ask()
    elif answer == "help":
        print(
            f'\nhelp is coming soon! (Probably in verson 2.5. This is only version {version})\n'
        )
        ask()
    elif answer == "exit":
        print("\nExiting Program...")
        sleep(1)

foodslist = FoodsList()
ask()
