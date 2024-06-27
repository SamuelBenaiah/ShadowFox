import random

# Define the number of rolls
num_rolls = 20

# Initialize counters
count_6 = 0
count_1 = 0
count_two_6s_in_a_row = 0

# Variable to keep track of the previous roll
previous_roll = None

# Simulate rolling the die
for _ in range(num_rolls):
    roll = random.randint(1, 6)

    # Update counters based on the roll
    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            count_two_6s_in_a_row += 1
    elif roll == 1:
        count_1 += 1

    # Update the previous roll
    previous_roll = roll

# Print the statistics
print(f"Number of times rolled a 6: {count_6}")
print(f"Number of times rolled a 1: {count_1}")
print(f"Number of times rolled two 6s in a row: {count_two_6s_in_a_row}")
