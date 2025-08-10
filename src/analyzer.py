import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
file_path = os.path.join(os.path.dirname(__file__), "..", "data", "students.csv")
file_path = os.path.abspath(file_path)
df = pd.read_csv(file_path)

# Calculate total & average
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Highest & lowest scorers
highest_scorer = df.loc[df["Total"].idxmax()]
lowest_scorer = df.loc[df["Total"].idxmin()]

# Save results
os.makedirs("output", exist_ok=True)
with open("output/results.txt", "w") as f:
    f.write("📊 Student Marks Analysis\n")
    f.write("=" * 30 + "\n\n")
    f.write(f"Highest Scorer: {highest_scorer['Name']} ({highest_scorer['Total']} marks)\n")
    f.write(f"Lowest Scorer: {lowest_scorer['Name']} ({lowest_scorer['Total']} marks)\n\n")
    f.write("Full Data:\n")
    f.write(df.to_string(index=False))

# Plot marks distribution
plt.figure(figsize=(8, 5))
df.plot(x="Name", y=["Math", "Science", "English"], kind="bar")
plt.title("Marks Distribution by Subject")
plt.ylabel("Marks")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("output/marks_distribution.png")
plt.show()
