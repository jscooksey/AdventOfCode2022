# Set the scoring
outcome_score = {"A X": 3, "A Y": 6, "A Z": 0, "B X": 0, "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3}

shape_score = {"X": 1, "Y": 2, "Z": 3}

# Set working variables
total = 0

# Read all lines
with open("input.txt") as f:
    lines = f.read().splitlines()

# Loop through lines
for line in lines:
    # Calculate point for this round
    points = outcome_score[line] + shape_score[line[-1]]
    # Update total
    total = total + points

# Print out total
print(f"You made {total} points")
