#https://github.com/hhbo62/Restaurant-Order-Program
#Add: openFiles.py (after finished) Add: acurate totals.
#note: this is the main program. All other files are test files (except stats.txt).
from time import sleep

#Version
version = 0.5

about_screen = f"""
\tThis is Resturaunt Order Program v.{version}
\tMade by me (obviously)

\n\tVersion {version} is here!
\tAdded:
\t\tMore efficient program code using dictionarys
\t\tAbout page
\t\tStart Menu
\n\tComing Soon:\n
\t\tHelp page
\t\tProgram Loops more than once
\t\tEven MORE efficient program; re-write ENTIRE code and use modules and classes
\t\tA GUI
\t\tA website
\n\tUgrent Updates:\n
\t\tThe Total Prices and total calories don't work (and I can't figure out how to fix 'em!!!!
"""

#Class
class FoodsList():
    def __init__(self):
        items = []
        
    def addFood(self, foodObject):
        items.append(foodObject)

        
    def getTotal(self):
        total = 0
        for item in item:
            total += getPrice(item)
            return
        

class Food():
    def __init__(self, food, qt, price, cal):
        self.food = food
        self.qt = qt
        self.price = price
        self.cal = cal
        
        
    def getPrice(self):
        return self.price * self.qt
    
    def getQt(self):
        return self.qt
    
    def getCal(self):
        return self.cal
        

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
    if sandwhich.getQt> 0:
        if sandwhich.getQt == 1:
            print("One Sandwich")
        else:
            print(f'Sandwiches: {sandwich_answer["qt"]}')

    if pancake_answer["qt"] > 0:
        if pancake_answer["qt"] == 1:
            print("One Pancake")
        else:
            print(f'Pancakes: {pancake_answer["qt"]}')

    if se_answer["qt"] > 0:
        if se_answer["qt"] == 1:
            print("One Scrambled Egg")
        else:
            print(f'Scrambled Eggs: {se_answer["qt"]}')

    if be_answer["qt"] > 0:
        if be_answer["qt"] == 1:
            print("One Boiled Egg")
        else:
            print(f'Boiled Eggs: {be_answer["qt"]}')

    if bp_answer["qt"] > 0:
        if bp_answer["qt"] == 1:
            print("One Breakfast Pizza")
        else:
            print(f'Breakfast Pizzas: {bp_answer["qt"]}')

    #total price+Cal
    total_price = sandwich_answer["price"] + pancake_answer[
        "price"] + se_answer["price"] + be_answer["price"]

    print(f'Total: ${total_price}')

    total_cal = "global"
    total_cal = sandwich_answer["calories"] + pancake_answer[
        "calories"] + se_answer["calories"] + be_answer["calories"]

    print(f'Calories: {total_cal}')


#run
def run_program():
    print("\n\tResturant Order Form:")
    take_order()
    confirm()


#ask
def ask():
    print("\n\tWelcome to Resturaunt Order Program!")
    start_about_help = input(
        f'\n\nGitHub: https://github.com/hhbo62/Restaurant-Order-Program\nThis is version {version}.\n\nType [start] to start program. \nType[About] to go to the about screen (and see what changed in the new update). \nType [help] to go to help. \nType [exit] to exit program. '
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


ask()
foodslist = FoodsList()
food = Food()
#issubclass
