num = input("Enter a number: ")
with open("output.txt", "w") as f:
    f.write(f"You entered: {num}\n")

with open("output.txt", "a") as f:
    f.write("More data.\n")

with open("output.txt") as f:
    print(f.read(), end='')
