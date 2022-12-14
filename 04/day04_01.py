import re

# Read all lines
with open("input.txt") as f:
    lines = f.read().splitlines()
# Set local varibale
total = 0

# Loop through all assignments
for line in lines:
    # Convert to array of integers
    x = re.findall("[0-9]+", line)
    numbers = list(map(int, x))

    # If either pair contains the other increment counter
    if numbers[2] <= numbers[0] <= numbers[3] and numbers[2] <= numbers[1] <= numbers[3]:
        total = total + 1
    elif numbers[0] <= numbers[2] <= numbers[1] and numbers[0] <= numbers[3] <= numbers[1]:
        total = total + 1

# Results
print(f"Total assignment pairs contained in the other is {total}")
