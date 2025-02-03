import random

def choose_word():
    words = ['python', 'developer', 'hangman', 'computer', 'programming', 'software']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord: " + display_word(word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
        
        guess = input("Guess a letter: ").strip().lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("🎉 Congratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print(f"❌ Incorrect! You have {attempts} attempts left.")
    
    if attempts == 0:
        print("💀 Game over! The word was:", word)

    # Ask if user wants to play again
    if input("\nDo you want to play again? (y/n): ").strip().lower() == 'y':
        hangman()

if __name__ == "__main__":
    hangman()
