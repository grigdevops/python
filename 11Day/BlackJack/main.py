
import random


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""






def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    "Choose random card from the deck."
    card = random.choice(cards)
    return card









def calculate_score(player_cards):
    print(player_cards)

    if sum(player_cards) == 21 and len(player_cards)==2:
        return 0
    if sum(player_cards) > 21 and 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)

    return sum(player_cards)



def compare(user_score, computer_score):

    if user_score > 21 and computer_score > 21:
        return "You went over . Your Lose"

    if user_score == computer_score:
        "Draw the cards"
    elif computer_score == 0:
        print("Computer WIN The Game")
    elif user_score == 0:
        print("User WIN the game, you have BlackJack")
    elif user_score > 21:
        "User lose the game"
    elif computer_score > 21:
        "Computer Lose the Game"
    elif user_score > computer_score:
        return "User win the game"
    else:
        return "Computer win the game"



def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    continue_game = True

    for i in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while continue_game:
        u_score = calculate_score(user_cards)
        p_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score : {u_score}")
        print(f"Computer's first card : {p_score}")

        if u_score == 0 or p_score == 0 or u_score > 21:
            continue_game = False
        else:
            draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_card == 'y':
                user_cards.append(deal_card())
            else:
                continue_game = False

    while p_score != 0 and p_score < 17:
        computer_cards.append(deal_card())
        p_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {u_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {p_score}")
    print(compare(u_score, p_score))






while input("Do you want to play a game of BlackJack? type 'y' or 'n': ") == 'y':
    play_game()






