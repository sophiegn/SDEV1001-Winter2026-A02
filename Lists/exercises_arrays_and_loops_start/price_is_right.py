import random

print("Welcome to the Price is Right! Guess the price of this coffee")
price = [random.randint(1,10),random.randint(1,10),random.randint(1,10)]

guess = input("Guess the price of the item: ")

if guess != price:
    print("You lose!")
    print("The price was: ")
    print(price)
elif guess == price:
    print("You win!")
    print("The price was: ")
    print(price)