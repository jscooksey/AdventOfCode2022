# Set the scoring
shape_score = {"A X": 3, "A Y": 1, "A Z": 2, "B X": 1, "B Y": 2, "B Z": 3, "C X": 2, "C Y": 3, "C Z": 1}

outcome_score = {"X": 0, "Y": 3, "Z": 6}

# Set working variables
total = 0

# Read all lines
with open("input.txt") as f:
    lines = f.read().splitlines()

# Loop through the lines
for line in lines:
    points = outcome_score[line[-1]] + shape_score[line]
    total = total + points
    # print(f"{line} = {points} points. Total now {total}")

# Print out the total
print(f"You made {total} points")
