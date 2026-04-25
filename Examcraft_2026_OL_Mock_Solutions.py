# ============================================================
# Examcraft 2026 Pre-Leaving Certificate Mock - Ordinary Level
# Computer Science Section C - Programming Solutions
# ============================================================


# ------------------------------------------------------------
# Question 16(a) - Step Tracker App
# ------------------------------------------------------------

print("Welcome to the Step Tracker App!")

# Part (iii) - Ask user for their name
name = input("Please enter your name: ")

# Part (i) - Comment on the input line
steps_today = int(input("Enter the number of steps you walked today: ")) #this is where the user enters the number of steps

# Part (iv) - Handle negative steps
if steps_today < 0:
    print("The number of steps cannot be negative")

# Part (v) - Categorise the user's day
elif steps_today < 5000:
    print(f"Try to be more active today {name}")
elif steps_today < 10000:
    print(f"Good effort {name}! Almost there.")
else:
    print(f"Well done {name} you reached your goal!")


# ------------------------------------------------------------
# Question 16(b) - Weekly Step Tracker
# ------------------------------------------------------------

print("Welcome to my weekly step tracker!")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps_list = []

for day in days:
    steps = int(input(f"Please enter the steps you did on {day}: "))
    steps_list.append(steps)

print("The list of steps is:", steps_list)
print("The total steps taken this week was:", sum(steps_list))
print("The average number of steps is:", round(sum(steps_list) / len(steps_list), 2))
print("The largest number of steps you took this week was:", max(steps_list))
print("The smallest number of steps you took this week was:", min(steps_list))
