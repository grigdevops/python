from menu import MENU

Water = 300
Milk = 200
Coffee = 100
Money = 0

quarters = 0.25
dimes = 0.1
nickles = 0.05
pennies = 0.01

def process_coins(quarters_entered,dimes_entered,nickles_entered,pennies_entered):
    global quarters
    global dimes
    global nickles
    global pennies
    summary_money = quarters*quarters_entered + dimes*dimes_entered + nickles*nickles_entered + pennies*pennies_entered

    return summary_money

def check_resources(coffee):
    global Water
    global Milk
    global Coffee
    global Money
    sufficient_resources = True
    print("Please insert coins.")
    quarters_customer = int(input("how many quarters?: "))
    dimes_customer = int(input("how many quarters?: "))
    nickles_customer = int(input("how many quarters?: "))
    pennies_customer = int(input("how many quarters?: "))
    money = process_coins(quarters_customer, dimes_customer, nickles_customer, pennies_customer)
    if money >= MENU[coffee]["cost"]:
        while sufficient_resources:
           Water -= MENU[coffee]["indredients"]["water"]
           print(Water)
           Milk -= MENU[coffee]["indredients"]["milk"]
           print(Milk)
           Coffee -= MENU[coffee]["indredients"]["coffee"]
           print(Coffee)
           if Water < 0:
               print("Sorry there is not enough water.")
               sufficient_resources = False
           elif Milk < 0:
               print("Sorry there is not enough water.")
               sufficient_resources = False
           elif Coffee < 0:
               sufficient_resources = False
               print("Sorry there is not enough water.")
           else:
               Money += MENU[coffee]["cost"]
               print(f"Here is ${money-Money} in change.")
               print(f"Here is your {coffee} ☕️. Enjoy!")
               sufficient_resources = False

    elif money < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        return "Sorry you entered wrong choice."



coffe_select = input("What would you like? (espresso/latte/cappuccino):")
check_resources(coffe_select)

