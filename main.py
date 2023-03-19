from random import choice


def game():
    user_name = input('Enter your name: ')
    print(f"Hello, {user_name}")

    with open('rating.txt', 'r') as ratings:
        for row_index, row in enumerate(ratings):
            if user_name in row:
                row = row.split(' ')
                user_rating = int(row[1])
                break
            else:
                user_rating = 0

    game_options = ['rock', 'paper', 'scissors']

    victory_conditions = {}

    for key_name in game_options:
        key_name_index = game_options.index(key_name)
        weak_list = game_options[key_name_index + 1:] + game_options[:key_name_index]
        weak_list = weak_list[:int(len(weak_list) / 2)]
        victory_conditions[key_name] = weak_list

    print("Okay, let's start")

    while True:
        print("Please enter 'rock', 'paper', 'scissors', '!exit', or '!rating'")
        user_choice = input()
        computer_choice = choice(list(game_options))

        if user_choice == '!exit':
            print('Bye!')

            with open('rating.txt', 'w') as ratings:
                ratings.write(f"{user_name} {user_rating}")

            exit()

        elif user_choice == '!rating':
            print(f"Your rating: {user_rating}")
            continue

        elif user_choice not in game_options:
            print('Invalid input')
            continue

        elif user_choice == computer_choice:
            print(f"There is a draw ({user_choice})")
            user_rating += 50

        elif user_choice in victory_conditions[computer_choice]:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_rating += 100

        elif user_choice not in victory_conditions[computer_choice]:
            print(f"Sorry, but the computer chose {computer_choice}")


if __name__ == '__main__':
    game()
