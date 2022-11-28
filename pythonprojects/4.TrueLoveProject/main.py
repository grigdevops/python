print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()


t_count1 = name1_lower.count("t")
r_count1 = name1_lower.count("r")
u_count1 = name1_lower.count("u")
e_count1 = name1_lower.count("e")



l_count1 = name1_lower.count("l")
o_count1 = name1_lower.count("o")
v_count1 = name1_lower.count("v")


t_count2 = name2_lower.count("t")
r_count2 = name2_lower.count("r")
u_count2 = name2_lower.count("u")
e_count2 = name2_lower.count("e")


l_count2 = name2_lower.count("l")
o_count2 = name2_lower.count("o")
v_count2 = name2_lower.count("v")


tot_t = t_count2 + t_count1
tot_r = r_count2 + r_count1
tot_u = u_count2 + u_count1
tot_e_t = e_count2 + e_count1

total_true = tot_t + tot_r + tot_u + tot_e_t

tot_l = l_count2 + l_count1
tot_o = o_count2 + o_count1
tot_v = v_count2 + v_count1
tot_e_l = e_count2 + e_count1

total_love = tot_l + tot_o + tot_v + tot_e_l

str_total_true = str(total_true)
str_total_love = str(total_love)

match_str = str_total_true +  str_total_love
match_int = int(match_str)

if 10 < match_int < 90:
    print(f"Your score is {match_int}, you go together like coke and mentos.")
elif 40 < match_int < 50:
    print(f"Your score is {match_int}, you are alright together.")
else:
    print(f"Your score is {match_int}.")




# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
#
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e
#
# score = int(str(first_digit) + str(second_digit))
#
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")
