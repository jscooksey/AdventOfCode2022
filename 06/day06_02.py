# Imports

# Set local variables
marker_length = 14
x = 0

# Read all lines
with open("input.txt") as f:
    line = f.read()

# Read the first character block
quad = line[x : x + marker_length]
quad_set = set(quad)

# Loop through until charatcers are all distinct
while len(quad_set) != len(quad):
    x = x + 1
    quad = line[x : x + marker_length]
    quad_set = set(quad)

# Print the result
print(f"Sequence {quad} at position {x+marker_length}")
