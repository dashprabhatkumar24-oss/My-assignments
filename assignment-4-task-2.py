user_text = input("Enter some text to store in the file: ")
with open("output.txt", "w") as file:
    file.write(user_text + "\n")
print("Data written to output.txt")
additional_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_text + "\n")
print("Additional data appended to output.txt")
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
