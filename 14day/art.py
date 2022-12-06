import random
from game_data import data
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def random_player(data_of_players):
    random_player = random.choice(data_of_players)
    return random_player


def followers_count(player):
    followers_count = player["follower_count"]
    return followers_count


YOUR_SCORE = 0
def compare_followers(A_followers, B_followers, guess):
    global YOUR_SCORE
    if guess == "A" and A_followers > B_followers:
        YOUR_SCORE += 1
        print(YOUR_SCORE)
        return True
    elif guess == "B" and B_followers > A_followers:
        YOUR_SCORE += 1
        print(YOUR_SCORE)
        return True
    else:
        print(f"Sorry, that's wrong. Final score: {YOUR_SCORE}")
        return False

guess_correct = True
while guess_correct:
    A_player = random_player(data)
    print(A_player)
    B_player = random_player(data)
    print(B_player)
    A_foll_count = followers_count(A_player)
    print(A_foll_count)
    B_foll_count = followers_count(B_player)
    print(B_foll_count)
    question = input("Who has more followers? Type 'A' or 'B': ")
    measure = compare_followers(A_foll_count, B_foll_count, question)
    if measure == False:
        print("End of Game")
        guess_correct = False



