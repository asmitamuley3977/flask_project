import pandas as pd

# Read the CSV file
data = pd.read_csv("students.csv")

# Show the data
print("Student Data:")
print(data)

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Fill missing marks with average marks
data["Marks"] = data["Marks"].fillna(data["Marks"].mean())

# Fill missing age with average age
data["Age"] = data["Age"].fillna(data["Age"].mean())

# Show cleaned data
print("\nCleaned Data:")
print(data)

# Find students with marks above 80
print("\nStudents with marks above 80:")
print(data[data["Marks"] > 80])

# Find average marks of each course
print("\nAverage Marks by Course:")
print(data.groupby("Course")["Marks"].mean())

# Find highest marks
print("\nHighest Marks:")
print(data["Marks"].max())