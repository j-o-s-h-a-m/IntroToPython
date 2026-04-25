author = saksham joshi


print("******************")
print("*  Conversions   *")
print("******************")
print("1) From teaspoons to ml")
print("2) From tablespoons to ml")
print("3) From cups to ml")
print("4) From ml to teaspoons")
print("5) From ml to tablespoons")
print("6) From ml to cups")

conversion = int(input("Please enter conversion required from the menu, for example 1) to convert teaspoons to ml: "))

if conversion == 1:
    teaspoons = float(input("Please enter number of teaspoons: "))
    ml = teaspoons * 5
    print("The ml is:", ml)

elif conversion == 2:
    tablespoons = float(input("Please enter number of tablespoons: "))
    ml = tablespoons * 15
    print("The ml is:", ml)

elif conversion == 3:
    cups = float(input("Please enter number of cups: "))
    ml = cups * 240
    print("The ml is:", ml)

elif conversion == 4:
    ml = float(input("Please enter the number of ml: "))
    teaspoons = ml / 5
    print("The number of teaspoons is:", teaspoons)

elif conversion == 5:
    ml = float(input("Please enter the number of ml: "))
    tablespoons = ml / 15
    print("The number of tablespoons is:", tablespoons)

elif conversion == 6:
    ml = float(input("Please enter the number of ml: "))
    cups = ml / 240
    print("The number of cups is:", cups)

else:
    print("Invalid option. Please enter a number between 1 and 6.")



from datetime import datetime

prompt = input("Please enter prompt: ")

prompt_lower = prompt.lower()

if "hello" in prompt_lower:
    print("Hi there, how are you?")
elif "name" in prompt_lower:
    print("My name is ExamBot, how can I help?")
elif "time" in prompt_lower:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

elif "weather" in prompt_lower:
    print("It is always sunny in Ireland")

else:
    print("I am sorry, I do not know that one?")
