# ============================================================
# 2024 DEB Pre-Leaving Certificate - Ordinary Level
# Computer Science Section C - Programming Solutions
# ============================================================


# ------------------------------------------------------------
# Question 16(a) - Household Budget Calculator
# ------------------------------------------------------------

print("Household budget calculator.  Enter the following information:")

# Part (i) - Allow user to input number of adults and children
num_adults = int(input("Number of adults in household: "))
num_child = int(input("Number of children in household: "))

food_budget = 300
cost_food_adults = 50
cost_food_child = 35
child_allowance = 140

# Part (ii) - Extra €20 per child after the third child
if num_child > 3:
    extra_children = num_child - 3
    total_child_allowance = (child_allowance * num_child) + (extra_children * 20)
else:
    total_child_allowance = child_allowance * num_child

total_food_cost = (cost_food_adults * num_adults) + (cost_food_child * num_child)

# Part (iii) - Inflation rate input
inflation_rate = float(input("Inflation rate (e.g. 0.05 for 5% inflation): "))

print(f"Children's allowance total: \u20ac{total_child_allowance}")
print(f"Total household food cost: \u20ac{total_food_cost}")

# Part (iv) - Round inflation cost to 2 decimal places
food_cost_with_inflation = round(total_food_cost * (1 + inflation_rate), 2)
print(f"Total household food cost with inflation: \u20ac{food_cost_with_inflation}")

# Part (v) - Percentage spend on food
percentage_food = round((food_cost_with_inflation / total_child_allowance) * 100, 2)
print(f"Percentage spend on food: {percentage_food}%")

# Part (vi) - Budget remaining after food spend
budget_remaining = round(total_child_allowance - food_cost_with_inflation, 2)
print(f"Budget remaining after food spend: \u20ac{budget_remaining}")


# ------------------------------------------------------------
# Question 16(b) - 10-Year Investment Calculator
# ------------------------------------------------------------

principal = float(input("Enter the principal investment amount: \u20ac"))
rate = float(input("Enter the annual interest rate (e.g. 0.05 for 5% interest): "))

value = principal
for year in range(1, 11):
    value = round(value * (1 + rate), 2)
    print(f"Year {year} - Investment value: \u20ac{value}")
