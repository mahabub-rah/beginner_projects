import random
import time

# define decorators -- game
def game(func):
  def inner():
    print("Guess Any Number. You have 5 Changes")
    start_time = time.time()
    a = func()
    end_time = time.time()
    print("Your Guess Number", a)
    print(f"You take {round(end_time - start_time)} seconds")
  return inner()

# define the game
@game
def random_number():
  i = 5
  num =random.randint(1,100)
  l1 =[]
  while i > 0:
  # for the correct input
    try:
      guess = int(input('Write your number: '))
      i -=1
      if guess < num:
        print(f"You choose low Number. {i} {'attempt' if i <= 1 else 'attempts'} left.")
        l1.append(guess)
      elif guess>num:
        print(f"You choose high Number. {i} {'attempt' if i <= 1 else 'attempts'} left.")
        l1.append(guess)
      else:
        print('Congratulation! You win')
        break
        return l1
  # for the incorrect input
    except ValueError:
      print('Please write the correct number')
  # don't fill any above condition
  else:
      print('Loser! You lose')
      return l1
