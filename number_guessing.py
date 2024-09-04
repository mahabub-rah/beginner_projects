import random
lowest_number = int(input('Write your lowest number '))
highest_number = int(input('Write your highest number '))

number = (random.randint(lowest_number, highest_number))
print('You will get 7 Chances')
i = 0
guess_number = []
game_over =  False
while i<7:
    guess = int(input('Write your number '))
    i +=1
    if guess == number:
        game_over = True
    elif guess > number:
        print('Your Guess is very High')
        guess_number.append(guess)
    elif guess <number:
        print('Your Guess is very low')
        guess_number.append(guess)
if game_over:
     print('Congratulation! You win!.')
else:
    print('Game Over!---')
print(f"Guess Number: " , end = '\n ')
for n in guess_number:
        print(f"{n}", end = ' ')

