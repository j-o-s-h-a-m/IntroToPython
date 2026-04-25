author = saksham joshi


flight_num = input("Enter your flight number: ")
destination = input("Enter your destination: ")
num_ppl = int(input("Enter the number of people in the travel group: "))

num_children = int(input("Enter the number of children in the travel group: "))

print("Your flight number is", flight_num)
print("You are travelling to", destination)
print(f"There are {num_ppl} people in the travel group")

flight_upper = flight_num.upper()

if flight_upper == "EI121":
    price_per_person = 520
elif flight_upper == "EI125":
    price_per_person = 400
else:
    price_per_person = 520 

total_cost = (num_ppl * price_per_person) - (num_children * 50)

print(f"The total cost of your flights is \u20ac{total_cost}")




flight_number = input("Enter a flight number: ")

last_digit = flight_number[-1]

if last_digit == "2":
    print(f"Flight {flight_number} is a direct flight.")
elif last_digit == "5":
    print(f"Flight {flight_number} is an indirect flight (with stopover).")
else:
    print(f"Flight {flight_number} is not recognised.")
