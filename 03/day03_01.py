# Read all lines
with open("input.txt") as f:
    lines = f.read().splitlines()

# Set working variables
total = 0

# Loop through lines
for line in lines:
    # Split in to two equal strings
    items = int(len(line) / 2)
    a = line[:items]
    b = line[items:]

    # Find the common item
    common_item = list(set(a).intersection(b))[0]
    # Get priority value for it
    if common_item.islower():
        priority = ord(common_item) - 96
    else:
        priority = ord(common_item) - 38
    # Total
    total = total + priority

    # print(f"Common item is {common_item} and its priority is {priority} and total is {total}")


print(f"Total priority is {total}")
