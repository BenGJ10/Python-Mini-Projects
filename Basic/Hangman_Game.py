import random

words = [
    "Messi", "Ronaldo", "Neymar", "Mbappe", "Martinez",
    "DeBruyne", "Salah", "VanDijk", "Kane", "Hazard",
    "Mane", "Sterling", "Ramos", "Alisson", "Pedri",
    "Modric", "Suarez", "Benzema", "Aguero", "Aubameyang",
    "Dybala", "Haaland", "Zlatan", "Sancho", "Pogba",
    "Griezmann", "Coutinho", "Kimmich", "Pique", "Busquets",
    "Marcelo", "Alaba", "Rakitic", "Lukaku", "Firmino",
    "Fernandes", "Gomez", "Thiago", "Kroos", "Ozil",
    "Kante", "Son", "Verratti", "Chiellini", "Foden",
    "Hummels", "Laporte", "Godin", "Walker", "Cancelo",
    "Robertson", "Trent", "Silva", "Marquinhos", "Varane",
    "Pavard", "Skriniar", "Koulibaly", "Rudiger", "Carvajal",
    "Navas", "Courtois", "TerStegen", "Oblak", "Ederson",
    "Neuer", "Rashford", "Buffon", "Donnarumma", "Handanovic",
    "Onana", "Mendy", "Osimhen", "Saka", "Araujo",
    "Romero", "Rodri", "Kepa", "Pickford", "Vinicius",
    "Asensio", "Gavi", "Rodrygo", "Bale",
    "Casemiro", "Bellingham", "Isco", "Ziyech", "Pulisic",
    "Havertz", "Musiala", "Jorginho", "Gundogan", "Mahrez"
]

def play_game():
    word_choice = random.choice(words)
    word_display = ['_' for word in word_choice]
    attempts = 9
    tries = 0

    print("Welcome to the Footballers Hangman Game")
    print("---------------------------------------")
    print("RULES: You'll be given 9 attempts to guess the correct name!")


    while(attempts > 0 and '_' in word_display):
        print("\n" + " ".join(word_display))
        guess = input("\nGuess a letter: ").lower()
        if guess in word_choice:
            tries += 1
            for index, letter in enumerate(word_choice):
                if letter == guess:
                    word_display[index] = letter
        else:
            print("That letter doesn't appear in the word.\n")
            tries += 1
            attempts -= 1            

    if "_" not in word_display:
        print(f"You guessed the word correctly within {tries} tries!")
        print(" ".join(word_display))
    else:
        print("You lost, you ran out of choices!")
        print(f"The word was {word_choice}\n")

def main():
    while True:
        play_game()
        replay = input("Do you want to play again (y/n)? ").lower()
        if replay == "n":
            print("Thanks for playing, see you soon!")
            break

if __name__ == "__main__":
    main()