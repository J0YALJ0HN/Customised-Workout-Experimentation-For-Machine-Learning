import pandas as pd
import numpy as np

input_file = 'bodyPerformance.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(input_file)

# Define conditions for each difficulty level based on performance metrics and age
conditions = [
    ((df['age'] < 15) | (df['age'] > 55)),
    (df['bodyFat_'] > 25),
    ((df['gripForce'] < 30) | (df['situpsCounts'] < 20)),
    ((df['weight_kg'] > 100) & (df['bodyFat_'] < 15)),
    (df['broadJump_cm'] < 150)
]

# Assign difficulty levels based on the conditions
df['workout_difficulty'] = np.digitize(np.sum(conditions, axis=0), bins=[5, 4, 3, 2, 1, 0])

# Save the updated DataFrame to a new CSV file
output_file = 'bodyPerformance_with_difficulty_v2.csv'
df.to_csv(output_file, index=False)

print(f"Workout difficulty column added and saved to {output_file}")
