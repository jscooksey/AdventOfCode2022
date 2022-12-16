import re
from queue import LifoQueue

# Read all lines
with open("input.txt") as f:
    lines = f.read().splitlines()

# Initializing a stack
stacks = []
for i in range(9):
    stacks.append(LifoQueue(maxsize=72))


# Set regex to read in the current stacks
regex = r"[ \[]([ A-Z])[ \]] [ \[]([ A-Z])[ \]] [ \[]([ A-Z])[ \]] [ \[]([ A-Z])[ \]] [ \[]([ A-Z])[ \]] [ \[]([ A-Z])[ \]] [ \[]([ A-Z])[ \]] [ \[]([ A-Z])[ \]] [ \[]([ A-Z])[ \]]"

# Read in the current stacks into LIFO queue
for line in lines[8::-1]:
    # Convert to array of integers
    matched = re.search(regex, line)
    if matched:
        tokens = matched.groups()
        for index, val in enumerate(tokens):
            if val != " ":
                stacks[index].put(val)

# Set regex to read in the moves
regex = r"move (\d+) from (\d+) to (\d+)"

# Read in the moves and make the changes in the LIFO queues
for line in lines[10::]:
    matched = re.search(regex, line)
    if matched:
        tokens = matched.groups()
        numbers = list(map(int, tokens))
        for i in range(numbers[0]):
            item = stacks[numbers[1] - 1].get()
            stacks[numbers[2] - 1].put(item)

# Print out the top item in each stack
print("The top of the stacks contains:", end=" ")
for x in range(9):
    letter = stacks[x].get()
    print(letter, end="")

# Done
print(" Get to work elves!")
