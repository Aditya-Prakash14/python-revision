marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

# Ask for student name
name = input("Enter student name: ")

# Lookup and print result
if name in marks:
    print(f"{name} scored {marks[name]}")
else:
    print(f"No record found for {name}")
