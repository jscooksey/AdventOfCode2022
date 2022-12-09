# Question 1_2

# Read in all lines
with open("input.txt") as f:
    lines = f.read().splitlines()

# Create Variables
total = 0
totals = []

# Work through all lines
for line in lines:
    # If it is numerical add it to running total for this elf
    if line.isdigit():
        total = total + int(line)
    # Otherwise its a new elf so append last ones total and start again
    else:
        totals.append(total)
        total = 0

# Sort the totals from max downward
totals.sort(reverse=True)

# Print the sum of the top three totals (Answer)
print(f"The total Calories carried by the top the elves is {sum(totals[:3])}")
