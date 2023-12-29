import random
import time


class TextStyle:
    END = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'

# Game starting


rules_str = '\nRules: \n1. a random sequence of the items will be generated everytime you start the game. \n2. To win the game you have to pick every item in the right order. \n3. You cannot pick a single item twice. \n4. To pick the item you have to say "pick (item name)" and to drop it , you have to say "drop (item name)".\n5. There are 3 levels in this game - Easy , Medium and hard, you can pick any of those difficulty.\n6. And that is it! If you want to play the game type "play" or if you want to quit the game , type "quit"'

Easy = ['sword', 'gem', 'coins', 'gold']
Easy_shuffle = ['sword', 'gem', 'coins', 'gold']

Mid = ['sword', 'gem', 'coins', 'gold', 'silver', 'hammer', 'pickaxe']
Mid_shuffle = ['sword', 'Gem', 'coins', 'Gold', 'silver', 'hammer', 'pickaxe']

Hard = ['sword', 'gem', 'coins', 'gold', 'silver',
        'hammer', 'pickaxe', 'chicken', 'wood', 'metal']

Hard_shuffle = ['sword', 'gem', 'coins', 'gold', 'silver',
                'hammer', 'pickaxe', 'chicken', 'wood', 'metal']

picked = []


def gameStart():
    difficulty = str(
        input('Choose difficulty - \nE for easy ,M for medium, H for Hard : '))
    if difficulty.upper() == 'E':
        Easy_game()
    elif difficulty.upper() == 'M':
        Mid_game()
    elif difficulty.upper() == 'H':
        Hard_game()
    else:
        print('Invalid input , try again ')
        gameStart()


def Easy_game():
    random.shuffle(Easy_shuffle)
    won = False

    while won == False:
        if len(picked) == len(Easy):
            print('you have picked all the items available for you to pick but lets check if its the right order.... \n ')
            time.sleep(1)
            print('Working on it.... \n \n')
            time.sleep(0.5)
            for i in range(0, len(Easy_shuffle)):
                if picked[i] == Easy_shuffle[i]:
                    print(f'{TextStyle.BOLD}Congratulations , you have guessed it right! and you have won the game in easy mode {TextStyle.END}. \nNow i think you should try the Medium level.. ')
                    won = True
                    break
                elif picked[i] != Easy_shuffle[i]:
                    print(
                        'You didnt guessed it right , you can still try by dropping the items and re-arranging it all.. \n ')
                    print(f'This is the list of the items you picked {picked}')
                    break
        if not won:
            print(
                f'This is the list of the items you have to pick and drop {Easy} \n ')
            item = str(input(
                'Pick an item by entering "pick (item name) or drop it by entering "drop (item name) : \n'))
            item_value = item[5:]
            item_value.strip().lower()
            command = item[:4]
            command.strip().lower()

            if item_value.strip().lower() in Easy:
                if command == 'pick':
                    if item_value in picked:
                        print('you cannot pick an item twice.')

                    else:
                        picked.append(item_value)
                        print(
                            f"{TextStyle.ITALIC}These are the items that you have picked {TextStyle.END} \n{picked}\n ")

                elif command.strip().lower() == 'drop':
                    if item_value not in picked:
                        print(
                            'you cannot drop an item that has not been picked yet.\n ')

                    else:
                        picked.remove(item_value)
                    print(
                        f"These are the items that you have picked \n{picked}\n ")

            elif item_value not in Easy or command != 'pick' or 'drop':
                print('invalid item name try again')


def Mid_game():
    random.shuffle(Mid_shuffle)
    won = False

    while won == False:
        if len(picked) == len(Mid):
            print('you have picked all the items available for you to pick but lets check if its the right order.... \n ')
            time.sleep(1)
            print('Working on it.... \n \n')
            time.sleep(0.5)
            for i in range(0, len(Mid_shuffle)):
                if picked[i] == Mid_shuffle[i]:
                    print(f'{TextStyle.BOLD}Congratulations , you have guessed it right! and you have won the game in medium diffculty {TextStyle.END}. \nNow i think you should try the Hardest level...')
                    won = True
                    break
                elif picked[i] != Mid_shuffle[i]:
                    print(
                        'You didnt guessed it right , you can still try by dropping the items and re-arranging it all.. \n ')
                    print(f'This is the list of the items you picked {picked}')
                    break
        if not won:
            print(
                f'This is the list of the items you have to pick and drop {Mid} \n ')
            item = str(input(
                'Pick an item by entering "pick (item name) or drop it by entering "drop (item name) : \n'))
            item_value = item[5:]
            item_value.strip().lower()
            command = item[:4]
            command.strip().lower()

            if item_value in Mid:
                if command == 'pick':
                    if item_value in picked:
                        print('you cannot pick an item twice.')

                    else:
                        picked.append(item_value)
                        print(
                            f"{TextStyle.ITALIC}These are the items that you have picked {TextStyle.END} \n{picked}\n ")

                elif command == 'drop':
                    if item_value not in picked:
                        print(
                            'you cannot drop an item that has not been picked yet.\n ')

                    else:
                        picked.remove(item_value)
                    print(
                        f"These are the items that you have picked \n{picked}\n ")

            elif item_value not in Mid or command != 'pick' or 'drop':
                print('invalid item name try again')


def Hard_game():
    random.shuffle(Hard_shuffle)
    won = False

    while won == False:
        if len(picked) == len(Hard):
            print('you have picked all the items available for you to pick but lets check if its the right order.... \n ')
            time.sleep(1)
            print('Working on it.... \n \n')
            time.sleep(0.5)
            for i in range(0, len(Hard_shuffle)):
                if picked[i] == Hard_shuffle[i]:
                    print(f'{TextStyle.BOLD}Congratulations , you have guessed it right! and you have won the game in Hardest  Diffuclty !! {TextStyle.END}.')
                    won = True
                    break
                elif picked[i] != Hard_shuffle[i]:
                    print(
                        'You didnt guessed it right , you can still try by dropping the items and re-arranging it all.. \n ')
                    print(f'This is the list of the items you picked {picked}')
                    break
        if not won:
            print(
                f'This is the list of the items you have to pick and drop {Hard} \n ')
            item = str(input(
                'Pick an item by entering "pick (item name) or drop it by entering "drop (item name) : \n'))
            item_value = item[5:]
            item_value.strip().lower()
            command = item[:4]
            command.strip().lower()

            if item_value in Hard:
                if command == 'pick':
                    if item_value in picked:
                        print('you cannot pick an item twice.')

                    else:
                        picked.append(item_value)
                        print(
                            f"{TextStyle.ITALIC}These are the items that you have picked {TextStyle.END} \n{picked}\n ")

                elif command == 'drop':
                    if item_value not in picked:
                        print(
                            'you cannot drop an item that has not been picked yet.\n ')

                    else:
                        picked.remove(item_value)
                    print(
                        f"These are the items that you have picked \n{picked}\n ")

            elif item_value not in Hard or command != 'pick' or 'drop':
                print('invalid item name try again')

print(rules_str)

choice = str(input('Do you wanna play? : '))
if choice.lower().strip() == 'play' or choice.lower().strip() == 'yes':
    gameStart()
elif choice.lower().strip() == 'quit' or choice.lower().strip() == 'no':
    print('ok :(')
