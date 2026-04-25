# ============================================================
# 2023 DEB Pre-Leaving Certificate - Ordinary Level
# Computer Science Section C - Programming Solutions
# ============================================================


# ------------------------------------------------------------
# Question 16(a) - Airline Booking System
# ------------------------------------------------------------

# Part (i) - Allow variables to accept user input
flight_num = input("Enter your flight number: ")
destination = input("Enter your destination: ")
num_ppl = int(input("Enter the number of people in the travel group: "))

# Part (vi) - Ask for number of children (discount applies)
num_children = int(input("Enter the number of children in the travel group: "))

# Part (ii) - Print the values of the three variables
print("Your flight number is", flight_num)
print("You are travelling to", destination)
print(f"There are {num_ppl} people in the travel group")

# Part (iii) & (iv) - Calculate total cost based on flight number
# EI121 (or ei121) costs €520 per person, EI125 costs €400 per person
# Part (v) - Handle lowercase 'ei' using .upper()
flight_upper = flight_num.upper()

if flight_upper == "EI121":
    price_per_person = 520
elif flight_upper == "EI125":
    price_per_person = 400
else:
    price_per_person = 520  # default price for any other flight

# Part (vi) - Apply €50 discount per child
total_cost = (num_ppl * price_per_person) - (num_children * 50)

print(f"The total cost of your flights is \u20ac{total_cost}")


# ------------------------------------------------------------
# Question 16(b) - Sort Flights into Direct or Indirect
# ------------------------------------------------------------

# Flights ending in 2 fly direct; flights ending in 5 fly indirect
# Flight numbers: 122, 125, 132, 135, 155

flight_number = input("Enter a flight number: ")

# Check the last character of the flight number
last_digit = flight_number[-1]

if last_digit == "2":
    print(f"Flight {flight_number} is a direct flight.")
elif last_digit == "5":
    print(f"Flight {flight_number} is an indirect flight (with stopover).")
else:
    print(f"Flight {flight_number} is not recognised.")
