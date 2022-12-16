# Imports

# Read all characters
with open("input.txt") as f:
    line = f.read()

# Set local variables
total = 0

# Loop through until we find 4 unique characters in sequence
x = 0
quad = line[x : x + 4]
quad_set = set(quad)

while len(quad_set) != len(quad):
    x = x + 1
    quad = line[x : x + 4]
    quad_set = set(quad)

print(f"Sequence {quad} at position {x+4}")
