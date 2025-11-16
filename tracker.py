# Name: Omm Rout
# Date: 16/11/2025
# Assignment: Attendance Tracker using Python

print("---- Welcome to the Attendance Tracker Tool ----")
print("This tool will help store student names with their check-in time.\n")


attendance = {}

# Taking number of entries
count = int(input("How many attendance entries do you want to record? "))

for i in range(count):
    print(f"\nEntry {i + 1}:")
    
    # Taking student name
    name = input("Enter student name: ").strip()
    while name == "":
        print("Name cannot be empty. Please enter a valid name.")
        name = input("Enter student name: ").strip()
    
    # Check for duplicate name
    if name in attendance:
        print("This name already exists! Please enter a different student.")
        name = input("Enter student name again: ").strip()
    
    # Taking check-in time
    time = input("Enter check-in time (like 09:15 AM): ").strip()
    while time == "":
        print("Time cannot be empty. Please enter a valid time.")
        time = input("Enter check-in time: ").strip()

    attendance[name] = time


# Display Summary
print("\n\n------ Attendance Summary ------")
print("Student Name\t\tCheck-in Time")
print("-------------------------------------------")

for n, t in attendance.items():
    print(f"{n}\t\t{t}")

print("-------------------------------------------")
print("Total Students Present:", len(attendance))


# Absentee check
choice = input("\nDo you want to check absentees? (yes/no): ").lower()

if choice == "yes":
    total_students = int(input("Enter total number of students in the class: "))
    absentees = total_students - len(attendance)
    
    print("\nTotal Present:", len(attendance))
    print("Total Absent:", absentees)


# Save to file
save_file = input("\nDo you want to save the report to a file? (yes/no): ").lower()

if save_file == "yes":
    from datetime import datetime
    current_time = datetime.now()
    
    with open("attendance_log.txt", "w") as file:
        file.write("Attendance Report\n")
        file.write("------------------------------\n")
        for n, t in attendance.items():
            file.write(f"{n} - {t}\n")
        file.write("------------------------------\n")
        file.write(f"Total Present: {len(attendance)}\n")
        if choice == "yes":
            file.write(f"Total Absent: {absentees}\n")
        file.write("\nReport generated on: " + str(current_time))
    
    print("Attendance saved successfully in attendance_log.txt!")

print("\nThank you for using the Attendance Tracker Tool!")
