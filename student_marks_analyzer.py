import pandas as pd
import numpy as np

# Sample student marks data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 92, 78, 88, 76],
    'Science': [89, 94, 82, 90, 72],
    'English': [80, 85, 79, 92, 74]
}

# Create DataFrame
df = pd.DataFrame(data)

print("=== Student Marks Data ===")
print(df)

# Average marks per subject
print("\n=== Average Marks per Subject ===")
print(df[['Math', 'Science', 'English']].mean())

# Average marks per student
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)
print("\n=== Average Marks per Student ===")
print(df[['Name', 'Average']])

# Highest scoring student
top_student = df.loc[df['Average'].idxmax()]
print("\nTop Student:", top_student['Name'], "with average", top_student['Average'])

# Lowest scoring student
lowest_student = df.loc[df['Average'].idxmin()]
print("Lowest Student:", lowest_student['Name'], "with average", lowest_student['Average'])
