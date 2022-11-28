print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0


if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are 5$.")
    elif age <= 18:
        bill = 7
        print("Your tickets are $7.")
    elif age < 45:
        bill = 12
        print("Adult tickets are $12.")
    elif age <= 55 and age >= 45:
        bill = 0
        print(f"For peoples which is between age 45 and 55 all is free")
    print(f"Your final bill is {bill}")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")