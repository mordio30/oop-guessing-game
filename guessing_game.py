import random

class GuessingGame:
    def __init__(self, answer_number):
        
        self.answer_number = answer_number
        self.last_guess = None

    def guess(self, user_guess):
        
        self.last_guess = user_guess
        if user_guess < self.answer_number:
            return 'low'
        elif user_guess > self.answer_number:
            return 'high'
        else:
            return 'correct'

    def solved(self):
        
        return self.last_guess == self.answer_number



game = GuessingGame(random.randint(1, 100))  
last_guess = None
last_result = None

while not game.solved():
    if last_guess is not None:
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
        print("")  

    
    last_guess = int(input("Enter your guess: "))
    last_result = game.guess(last_guess)

print(f"{last_guess} was correct!")
