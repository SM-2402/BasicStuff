import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
begin_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

def blackjack():

    if begin_or_not == "y":
        game_over = False
        while not game_over:
            print(logo)           
            player_cards = random.choices(cards, k=2)
            computer_cards = random.choices(cards, k=2)
            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"computer's first card: {computer_cards[0]}")
            player_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            while sum(computer_cards)<17:
                computer_cards.append(random.choice(cards))

            if player_choice == "y":
                player_cards.append(random.choice(cards))
            print(player_cards)
            if 11 in player_cards:
                ace_value = input("You have an ace! Do you want assign it's value to be '1' or '11'? ")
                if ace_value == 1:
                    player_cards[player_cards.index(11)] = 1

            player_final_score = sum(player_cards)
            computer_final_score = sum(computer_cards)
            print(f"Your final hand: {player_cards}, final score: {player_final_score}")

            if player_final_score >21:
                print(f"Computer's final hand: [{computer_cards[0]}], final score: {computer_cards[0]}")
                print("You went over. You loose !")
            elif player_final_score <=21 and computer_final_score<=21:
                print(f"Computer's final hand: {computer_cards}, final score: {computer_final_score}")
                if computer_final_score < player_final_score:
                    print("You win!")
                elif computer_final_score == player_final_score:
                    print("Draw!")
                else:
                    print("You loose!")

            elif player_final_score<=21 and computer_final_score>21:
                print(f"Computer's final hand: {computer_cards}, final score: {computer_final_score}")
                print("You win!")

            play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
            if play_again == "n":
                game_over = True

            else:
                print("\n" * 20)
                blackjack()



    else:
        return



blackjack()
