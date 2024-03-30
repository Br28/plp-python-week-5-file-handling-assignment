# File Creation
with open("my_file.txt", "w") as file:
    file.write("Hello, this is line 1.\n")
    file.write("12345\n")
    file.write("Line 3 contains both text and numbers: abc123\n")

# File Reading and Display
with open("my_file.txt", "r") as file:
    contents = file.read()
    print("Contents of my_file.txt:")
    print(contents)

# File Appending
with open("my_file.txt", "a") as file:
    file.write("This is line 4, appended.\n")
    file.write("Another line appended.\n")
    file.write("The last appended line.\n")

# Error Handling
try:
    with open("non_existent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("This block always executes, regardless of exceptions.")
