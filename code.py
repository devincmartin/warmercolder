# Your code here!
import random
guess = int(input("Guess the number "))
count = 0
n = random.randint(0,100)
prev_guess = -1

if guess > n - 10 and guess < n + 10:
  print("you are red hot")
elif guess > n - 20 and guess < n + 20:
  print("you are warm")
elif guess > n + 20 or guess < n - 20:
  print("you are cold")
    
while guess != n:

  
  if count >= 1:

    if abs(n - guess) < abs(n - prev_guess):
      print("You are getting warmer")
    else:
      print("You are getting colder")

    if guess > n - 10 and guess < n + 10:
      print("you are red hot")
    elif guess > n - 20 and guess < n + 20:
      print("you are warm")
    elif guess > n + 20 or guess < n - 20:
      print("you are cold")

  
  count += 1
  prev_guess = guess
  guess = int(input("Guess the number "))

count += 1
print("You are correct! You got it after" , count, "guesses.")

    
