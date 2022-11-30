from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():

    random_card = random.choices(cards, k=1)
    return random_card


def sum_of_cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_sum, computer_sum):

    if user_sum > 21  and computer_sum > 21:
        return "Both went over . You lose but"

    if user_sum == computer_sum:
        return "Draw "
    elif computer_sum == 0:
        return "Lose, opponent has BlackJack"
    elif user_sum == 0:
        return "Win with a BlackJack"
    elif user_sum > 21:
        return "You went over, PC win "
    elif computer_sum > 21:
        return "Win with a BlackJack, opponent went over"
    elif user_sum > computer_sum:
        return "You win "
    else:
        return "You Lose"

def play_game():
    print(logo)



    user_cards = random.choices(cards, k=2)
    print(user_cards)
    computer_cards = random.choices(cards, k=2)
    print(computer_cards)
    final_of_game = False


    while not final_of_game:
        sum_user = sum_of_cards(user_cards)
        sum_computer = sum_of_cards(computer_cards)

        print(f" Your Cards: {user_cards}, current score: {sum_user}")
        print(f" Computer's first card: {computer_cards[0]}")

        if sum_user == 0 or sum_computer == 0 or sum_user > 21:
            final_of_game = True
        else:
            user_continue = input("Type 'Y' to get another card, type 'N' to pass")
            if user_continue == 'Y':
                user_cards.append(deal_card())
            else:
                final_of_game = True


    while sum_computer != 0 and sum_computer < 17:
        computer_cards.append(deal_card())
        sum_computer = sum_of_cards(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {sum_user}")
    print(f"   Computer's final hand: {computer_cards}, final score: {sum_computer}")
    print(compare(sum_user, sum_computer))

while input("Type 'Y' to get another card, type 'N' to") == "Y":
    play_game()












