# Define function to calculate priorities
def item_value(item) -> int:
    if item.islower():
        priority = ord(item) - 96
    else:
        priority = ord(item) - 38
    return priority


# Read all lines
with open("input.txt") as f:
    lines = f.read().splitlines()

# Set working variables
total = 0

# Loop through all groups (3 lines)
for x in range(0, len(lines), 3):

    # Get the pack item lists
    pack_1 = lines[x]
    pack_2 = lines[x + 1]
    pack_3 = lines[x + 2]

    # Calculate the common item
    common_item = list(set(pack_1).intersection(pack_2).intersection(pack_3))[0]
    priority = item_value(common_item)

    total = total + priority

    # print(f"At {x} the common item is {common_item} whos value is {priority} and total is now {total}")

print(f"Total priority is {total}")
