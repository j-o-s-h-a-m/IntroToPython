author = saksham joshi
num2 = float(input("Please enter your second number: "))

if option == "a":
    result = num1 + num2
    print(f"{num1} + {num2} = {round(result, 2)}")

elif option == "s":
    result = num1 - num2
    print(f"{num1} - {num2} = {round(result, 2)}")

elif option == "m":
    result = num1 * num2
    print(f"{num1} x {num2} = {round(result, 2)}")

elif option == "d":
    result = num1 / num2
    print(f"{num1} / {num2} = {round(result, 2)}")



import random

words = ["cat", "mat", "can", "man", "pool", "tool", "mule", "pat", "tan", "rule"]
print("The list of words is: ", words)

random_word = words[random.randint(0, len(words) - 1)]

print("The length of the word is:", len(random_word))


print("The first letter in the word is:", random_word[0].upper())

guessed = False
for attempt in range(3):
    guess = input("Please guess what the word is: ")
    if guess == random_word:
        print("Well done!")
        print("The word was:", random_word)
        guessed = True
        break
    else:
        if attempt < 2:
            print("You guessed incorrectly, try again")

if not guessed:
    print("You guessed incorrectly, try again")
    print("The word was:", random_word)
