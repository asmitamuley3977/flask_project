import os
import shutil
import csv

# Create folders
os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)


# 1. Create and write a text file
try:
    with open("input/sample.txt", "w") as file:
        file.write("Hello, this is my Python project.")
        file.write("\nI am learning file handling.")

    print("Text file created successfully.")

except Exception as e:
    print("Error:", e)


# 2. Read the text file
try:
    with open("input/sample.txt", "r") as file:
        data = file.read()

    print("\nText file content:")
    print(data)

except Exception as e:
    print("Error:", e)


# 3. Create and write a CSV file
try:
    with open("input/students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Age", "Course"])
        writer.writerow(["Asmita", 20, "Computer Science"])
        writer.writerow(["Rahul", 21, "Computer Science"])

    print("\nCSV file created successfully.")

except Exception as e:
    print("Error:", e)


# 4. Read the CSV file
try:
    print("\nCSV file content:")

    with open("input/students.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

except Exception as e:
    print("Error:", e)


# 5. Rename the text file
try:
    os.rename("input/sample.txt", "input/new_sample.txt")
    print("\nFile renamed successfully.")

except Exception as e:
    print("Error:", e)


# 6. Move the file
try:
    shutil.move("input/new_sample.txt", "output/new_sample.txt")
    print("File moved successfully.")

except Exception as e:
    print("Error:", e)


# 7. Delete the file
try:
    os.remove("output/new_sample.txt")
    print("File deleted successfully.")

except Exception as e:
    print("Error:", e)


print("\nProject completed successfully!")