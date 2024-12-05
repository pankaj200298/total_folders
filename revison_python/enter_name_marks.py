n = int(input("Enter the number of students: "))
d = {}

# Input data for each student
for i in range(n):
    name = input(f"Enter the name of student {i + 1}: ")
    marks = int(input(f"Enter the marks for student {i + 1}: "))
    d[name] = marks  # Store the student's data in the dictionary

# Loop for retrieving data
while True:
    name = input("Enter the name of the student to display marks: ")
    marks = d.get(name, -1)  # Fetch marks or return -1 if name not found
    if marks == -1:
        print("This student is not present in the data.")
    else:
        print(f"Student Name: {name}, Marks: {marks}")

    option = input("Do you want to continue? [y/n]: ").strip().lower()
    if option == "n":
        break
    elif option == "y":
        continue
    else:
        print("Invalid option. Exiting...")
        break

# Print the dictionary (optional, for debugging)
print("Final Data:", d)
