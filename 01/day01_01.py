# Question 1

with open("input.txt") as f:
    lines = f.read().splitlines()

total = 0
current_max = 0

for line in lines:
    if line.isdigit():
        total = total + int(line)
    else:
        total = 0

    if total > current_max:
        current_max = total

print(f"Maximum Calories is {current_max}")
