expenses = []
n = int(input("Enter number of days: "))

for i in range(n):
    amt = float(input(f"Enter expense for day {i+1}: "))
    expenses.append(amt)

total = 0
highest = expenses[0]
lowest = expenses[0]
above_avg = 0

for e in expenses:
    total += e

    if e > highest:
        highest = e

    if e < lowest:
        lowest = e

average = total / n

for e in expenses:
    if e > average:
        above_avg += 1

print("\nExpense Data:", expenses)
print("Total Expense:", total)
print("Average Expense:", average)
print("Highest Expense:", highest)
print("Lowest Expense:", lowest)
print("Days Above Average Spending:", above_avg)

if average < 800:
    print("Spending Behavior: Low")
elif average <= 1500:
    print("Spending Behavior: Moderate")
else:
    print("Spending Behavior: High")
