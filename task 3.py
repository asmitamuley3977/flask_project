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



# output :
C:\Users\Asmita\AppData\Local\Programs\Python\Python310\python.exe "E:\asmis projects\alfido\task 3.py" 
Student Data:
     Name            Course  Marks  Age
0  Asmita  Computer Science   85.0   20
1   Rahul  Computer Science   78.0   21
2   Priya      Data Science   92.0   20
3    Amit      Data Science    NaN   21
4   Sneha  Computer Science   88.0   20
5   Rohan      Data Science   75.0   21
6    Neha  Computer Science   95.0   21

Missing Values:
Name      0
Course    0
Marks     1
Age       0
dtype: int64

Cleaned Data:
     Name            Course  Marks  Age
0  Asmita  Computer Science   85.0   20
1   Rahul  Computer Science   78.0   21
2   Priya      Data Science   92.0   20
3    Amit      Data Science   85.5   21
4   Sneha  Computer Science   88.0   20
5   Rohan      Data Science   75.0   21
6    Neha  Computer Science   95.0   21

Students with marks above 80:
     Name            Course  Marks  Age
0  Asmita  Computer Science   85.0   20
2   Priya      Data Science   92.0   20
3    Amit      Data Science   85.5   21
4   Sneha  Computer Science   88.0   20
6    Neha  Computer Science   95.0   21

Average Marks by Course:
Course
Computer Science    86.500000
Data Science        84.166667
Name: Marks, dtype: float64

Highest Marks:
95.0

Process finished with exit code 0
