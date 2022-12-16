import re

# Read all lines
with open("input.txt") as f:
    lines = f.read().splitlines()

# Set local varibale
total = 0

# Loop through all assignment pairs
for line in lines:
    # Convert to array of integers
    x = re.findall("[0-9]+", line)
    numbers = list(map(int, x))

    # Check if the ranges cross at all
    if numbers[2] <= numbers[0] <= numbers[3] or numbers[2] <= numbers[1] <= numbers[3]:
        total = total + 1
    elif numbers[0] <= numbers[2] <= numbers[1] or numbers[0] <= numbers[3] <= numbers[1]:
        total = total + 1

# Print total
print(f"Total assignment pairs contained in the other is {total}")
