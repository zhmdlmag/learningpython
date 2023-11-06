import random
import hmwords
import hmart

stages = hmart.stages
print("Welcome to ...")
print(hmart.logo)

lives = len(stages) -1
end_of_game = False

word_list = hmwords.word_list

randomword = random.choice(word_list)
wordlen = len(randomword)

#display count
display = []
for letter in range(wordlen):
    display+='_'
    
print(f"{' '.join(display)}")

print(f"You got {lives} lives")

while not end_of_game:
    guess = input("Guess the word, type the letter: ").lower()
    #check guessed letter
    
    if guess in display:
        print(f"You've already guessed {guess}")
    
    for pos in range (wordlen):
        letter = randomword[pos]
        if letter == guess:
            display[pos] = letter

    if guess not in randomword:
        print(f"You guessed {guess}")
        lives -=1
        print(f"Incorrect! You got {lives} lives left")
        if lives == 0:
            end_of_game = True
            print(f"You lost :( \nThe word was {randomword}!")
            
    print(f"{' '.join(display)}")
    
    if '_' not in display:
        end_of_game = True
        print("You Won")
        
    print(stages[lives])
    
