import os
import random
import sys


class bcolors:
    PURPLE = '\033[35m'
    BLUE = '\033[34m'
    BLUEBG = '\033[44m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    GREENBG = '\033[42m'
    PINK = '\033[95m'
    RED = '\033[91m'
    REDBG = '\033[41m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def select_difficulty():
    while True:
        user_choice = input(
            "\nHow do you like your game?\n\n[1] Easy\n[2] Medium\n[3] Hard\n[4] Extremely Hard\n[5] Quit\n\nPlease enter (1-5): ")
        if user_choice in ("1", "2", "3", "4", "5"):
            if user_choice == "1":
                word_length = 5
                max_chances = 6
                word_length_en = f"a {bcolors.BOLD + bcolors.PINK}five{bcolors.ENDC}-letter word"
                break
            elif user_choice == "2":
                word_length = 6
                max_chances = 6
                word_length_en = f"a {bcolors.BOLD + bcolors.PINK}six{bcolors.ENDC}-letter word"
                break
            elif user_choice == "3":
                word_length = 8
                max_chances = 6
                word_length_en = f"an {bcolors.BOLD + bcolors.PINK}eight{bcolors.ENDC}-letter word"
                break
            elif user_choice == "4":
                word_length = 10
                max_chances = 8
                word_length_en = f"a {bcolors.BOLD + bcolors.PINK}ten{bcolors.ENDC}-letter word"
                break
            elif user_choice == "5":
                sys.exit("\nSorry to see you go. Bye!\n")

        else:
            print("\nInvalid input. Please try again.\n")

    return word_length, word_length_en, max_chances


def word_to_list(any_word):
    letter_list = []
    for i in any_word:
        letter_list.append(i)
    return letter_list


print("")
print(f"{bcolors.BOLD + bcolors.GREEN}*{bcolors.ENDC}" * 18)
print(f"{bcolors.BOLD + bcolors.YELLOW}*{bcolors.ENDC}" * 18)
print(f"{bcolors.BOLD + bcolors.RED}*  GUESS A WORD  *{bcolors.ENDC}")
print(f"{bcolors.PURPLE}* by  Jason Shew *{bcolors.ENDC}")
print(f"{bcolors.PINK}* jason@shew.cc  *{bcolors.ENDC}")
print(f"{bcolors.BOLD + bcolors.BLUE}*{bcolors.ENDC}" * 18)
print(f"{bcolors.BOLD + bcolors.CYAN}*{bcolors.ENDC}" * 18 + "\n")

filename = "englishwords.txt"
dir = os.path.dirname(__file__)
file = os.path.join(dir, filename)

try:
    with open(file) as f:
        words = f.read().splitlines()
except OSError:
    sys.exit(
        f"FILE NOT FOUND\nPlease check {bcolors.BOLD + bcolors.PINK}{filename}{bcolors.ENDC} is in the same folder as this .py file.\n")

while True:
    word_length, word_length_en, max_chances = select_difficulty()
    print(f"\n{bcolors.RED + bcolors.BOLD + bcolors.UNDERLINE}RULES:\n{bcolors.ENDC}\n{bcolors.BLUE}1. {bcolors.ENDC} Enter {word_length_en} without hyphens, dots, or apostrophes.\n{bcolors.BLUE}2. {bcolors.ENDC} Correct letters are shown in {bcolors.BOLD + bcolors.GREENBG + bcolors.YELLOW}green{bcolors.ENDC}, misplaced ones in {bcolors.BOLD + bcolors.BLUEBG + bcolors.YELLOW}blue{bcolors.ENDC}, and wrong ones in {bcolors.BOLD + bcolors.REDBG + bcolors.YELLOW}red{bcolors.ENDC}.\n{bcolors.BLUE}3. {bcolors.ENDC} You have {bcolors.BOLD + bcolors.RED}{max_chances}{bcolors.ENDC} chances for each game.")
    print(f"\n{bcolors.PINK}Happy gaming!{bcolors.ENDC}\n")
    words_library = [word for word in words if len(word) == word_length]
    random_word = random.choice(words_library)
    guessed_words = []

    def inform_user():
        while True:

            list_given = word_to_list(random_word.upper())
            user_guess = input(
                f"Enter {word_length_en}: ").upper().strip().replace(" ", "")

            if user_guess.isalpha():
                if len(user_guess) == word_length:
                    if user_guess.casefold() in words:
                        if user_guess not in guessed_words:
                            guessed_words.append(user_guess)
                            break
                        else:
                            print("You just guessed that word. Try another one.")
                    else:
                        print(
                            f"""I don't think {user_guess} is an English word. Try again.""")
                else:
                    print(
                        f"""Sorry, {user_guess} is not {word_length_en}. Try again.""")
            else:
                print(
                    f"""Sorry, {user_guess} does not look like a normal word. :-( Maybe there was a typo?""")

        list_user = word_to_list(user_guess)
        user_result = []
        i = 0
        while i < word_length:

            if list_user[i] == list_given[i]:
                list_user[i] = list_user[i] + "RESOLVED"
                user_result.insert(i, list_user[i])
                list_given[i] = "RESOLVED"
                list_user[i] = "RESOLVED"

            else:
                user_result.insert(i, list_user[i])

            i += 1
        i = 0
        while i < word_length:
            if (list_user[i] in list_given) and (list_user[i] != "RESOLVED"):
                letter_index = list_given.index(list_user[i])
                list_given[letter_index] = "MISPLACED"
                user_result[i] = list_user[i] + "MISPLACED"

            elif list_user[i] not in list_given:
                user_result[i] = list_user[i] + "NONEXISTENT"
            else:
                pass
            i += 1
        y = 0
        for letter in user_result:
            if letter[1:] == "RESOLVED":
                y += 1
        if y == word_length:
            for n in random_word:
                print(bcolors.BOLD + bcolors.GREENBG + bcolors.YELLOW +
                      " " + n + bcolors.ENDC, end="")
            return [random_word, "SUCCESS"]
        else:
            for letter in user_result:
                if letter[1:] == "RESOLVED":
                    letter = letter.replace("RESOLVED", " ")
                    print(bcolors.BOLD + bcolors.GREENBG + bcolors.YELLOW +
                          " " + letter + bcolors.ENDC, end="")

                elif letter[1:] == "MISPLACED":
                    letter = letter.replace("MISPLACED", " ")
                    print(bcolors.BOLD + bcolors.BLUEBG + bcolors.YELLOW + " " +
                          letter + bcolors.ENDC, end="")

                elif letter[1:] == "NONEXISTENT":
                    letter = letter.replace("NONEXISTENT", " ")
                    print(bcolors.BOLD + bcolors.REDBG + bcolors.YELLOW + " " +
                          letter + bcolors.ENDC, end="")
            return [random_word, "FAIL"]

    attempt = 0
    chances_left = max_chances

    while attempt <= max_chances:
        chances_left = max_chances - attempt - 1
        random_word, final_result = inform_user()
        if final_result == "SUCCESS":
            print(
                f" |  WOW! YOU'RE {bcolors.RED}AMAZING{bcolors.ENDC}!!!\n{bcolors.ENDC}Yes, the word was {bcolors.BOLD + bcolors.GREENBG + bcolors.YELLOW + str(random_word.upper()) + bcolors.ENDC}!")
            break
        else:
            if chances_left > 1:
                print(
                    f" |  {bcolors.BOLD}{chances_left}{bcolors.ENDC} chances left")
            elif chances_left == 1:
                print(
                    f" |  {bcolors.BOLD + bcolors.RED}1 chance left{bcolors.ENDC}")
            else:
                print(
                    f" |  Sorry, you failed. The right word was {bcolors.BOLD + bcolors.GREENBG + bcolors.YELLOW}{random_word.upper()}{bcolors.ENDC}.")
                break

        attempt += 1

    while True:
        user_option = input("\nWanna play again? (Yes / No) ").lower()
        if user_option[0] in ("y", "yes", "n", "no"):
            break
        else:
            print("\nInvalid input. Please enter Y or N.\n")

    if user_option[0] == ("y" or "yes"):
        continue
    else:
        sys.exit("\nHope to see you again! Bye!\n")
