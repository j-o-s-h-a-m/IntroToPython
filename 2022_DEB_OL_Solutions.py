# ============================================================
# 2022 DEB Pre-Leaving Certificate - Ordinary Level
# Computer Science Section C - Programming Solutions
# ============================================================


# ------------------------------------------------------------
# Question 16(a) - Vaccine Registration Portal
# ------------------------------------------------------------

import random

while True:
    s_name = input("Enter your surname: ")
    f_name = input("Enter your first name: ")
    age = int(input("Enter your age: "))
    eircode = input("Enter your Eircode: ")

    # Determine vaccine type based on age (i, ii)
    if age >= 50:
        vaccine = "ADENO"
    else:
        vaccine = "MRNA"

    # Determine vaccination centre based on last digit of Eircode (iii)
    last_digit = int(eircode[-1])
    if last_digit % 2 != 0:
        centre = "Northfield"
    else:
        centre = "Eastwood"

    print(f"Hello {f_name} {s_name}, you are {age} years old and your Eircode is {eircode}.")
    print(f"You must attend {centre} for your vaccine")
    print(f"{f_name}, you will receive the {vaccine} vaccine")

    # Part (v) - vaccine trial enrolment
    trial = input("Do you agree to enrol in a vaccine trial?\nType 'Yes' or 'No' ")
    if trial == "Yes":
        super_vaccines = ["Super vaccine A", "Super vaccine B", "Super vaccine C"]
        assigned = random.choice(super_vaccines)
        print(f"You are now enrolled in the trial to receive {assigned}")

    # Part (iv) - while loop to continue or end
    cont = input("If you have finished entering people's details type 'END', otherwise press RETURN: ")
    if cont == "END":
        break


# ------------------------------------------------------------
# Question 16(b) - Find the Median Without Built-in Functions
# ------------------------------------------------------------

List1 = [4, 5, 9, 8, 10, 17, 99, 77]

# Sort the list manually using bubble sort
n = len(List1)
sorted_list = List1[:]
for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_list[j] > sorted_list[j + 1]:
            sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

print("Sorted list:", sorted_list)

# Find the median
if n % 2 == 0:
    mid1 = sorted_list[n // 2 - 1]
    mid2 = sorted_list[n // 2]
    median = (mid1 + mid2) / 2
else:
    median = sorted_list[n // 2]

print("The median of List 1 is:", median)
