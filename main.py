#Add: openFiles.py (after finished) Add: acurate totals
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
\t\tEven MORE efficient program; re-write ENTIRE code and use modules
\t\tA GUI
\t\tClasses
\n\tUgrent Updates:\n
\t\tThe Total Prices and total calories don't work (and I can't figure out how to fix 'em!!!!
"""

#Set up a dictionary for the accurate totals:
orders = {}

#Dictionary
sandwich_answer={
    "price":9.99,
    "calories":1500,
    "qt":0
}

pancake_answer={
    "price":2.99,
    "calories":400,
    "qt":0
}

se_answer={
    "price":5.99,
    "calories":600,
    "qt":0
}

be_answer={
    "price":5.00,
    "calories":600,
    "qt":0
}

bp_answer={
    "price":12.99,
    "calories":2000,
    "qt":0
}

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
    print(f'Sandwich: ({sandwich_answer["calories"]} calories, ${sandwich_answer["price"]})')
    sandwich_answer1 = input()
    sandwich_answer["qt"] = int(sandwich_answer1)
    orders['Sandwich'] = sandwich_answer["qt"]

    print(f'\nPancake: ({pancake_answer["calories"]} calories, ${pancake_answer["price"]})')
    pancake_answer1 = input()
    pancake_answer["qt"] = int(pancake_answer1)
    orders['Pancake'] = pancake_answer["qt"]

    print(f'\nScrambled Eggs: ({se_answer["calories"]} calories, ${se_answer["price"]})')
    se_answer1 = input()
    se_answer["qt"] = int(se_answer1)
    orders['Scrambled Eggs'] = se_answer["qt"]

    print(f'\nBoiled Eggs: ({be_answer["calories"]} calories, ${be_answer["price"]})')
    be_answer1 = input()
    be_answer["qt"] = int(be_answer1)
    orders['Boiled Eggs'] = be_answer["qt"]
 
    print(f'\nBreakfast Pizza: ({bp_answer["calories"]} calories, ${bp_answer["price"]})')
    bp_answer1 = input()
    bp_answer["qt"] = int(bp_answer1)
    orders['Breakfast Pizza'] = bp_answer["qt"]
 
    print(f' \n\tYour Order:\n')
    
    #to display or not to display. That is the question
    if sandwich_answer["qt"] > 0:
        if sandwich_answer["qt"] == 1:
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
    total_price = "global"
    total_price = sandwich_answer["price"] + pancake_answer["price"] + se_answer["price"] + be_answer["price"]

    print(f'Total: ${total_price}')

    total_cal = "global"
    total_cal = sandwich_answer["calories"] + pancake_answer["calories"] + se_answer["calories"] + be_answer["calories"]

    print(f'Calories: {total_cal}')

#run
def run_program():
    print("\n\tResturant Order Form:") 
    take_order()
    confirm()

#ask
def ask():
	print("\n\tWelcome to Resturaunt Order Program!")
	start_about_help = input(f'This is version {version}. \n\nType [start] to start program. \nType[About] to go to the about screen (and see what changed in	the new update). \nType [help] to go to help. ')

	answer = start_about_help.lower()
	start(answer)

#main running of program
def start(answer):
    
    if answer == "start":
        run_program()
        run_again = input("Type [run] to run again type [exit] to stop program ")
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
        print(f'\nhelp is coming soon! (Probably in verson 2.5. This is only version {version})\n')
        ask()
ask()
#issubclass