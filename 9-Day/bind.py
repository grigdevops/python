from art import logo

print(logo)

clean_the_screen = True


my_dict = {}
def dict_add(name_man, bid_price_bid):
    my_dict[name_man] = bid_price_bid


while clean_the_screen:
    choice = input("Are there any other users who want to play? ")


    if choice == "Yes":
        name = input("Please enter your name? ")
        bid_price = int(input("Please enter the Bid Price "))
        dict_add(name, bid_price)
    elif choice == "No":
        clean_the_screen = False
        max_value = 0
        for key in my_dict:
            if my_dict[key] > max_value:
                max_value = my_dict[key]
        print(max_value)
    else:
        print("You enter not correct choice")
        clean_the_screen = False


