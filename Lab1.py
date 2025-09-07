# Program Name: Lab1.py
# Course: IT1114/Section W01
# Student Name: Jessica Scales
# Assignment Number: Lab 1
# Due Date: 09/05/20X25
# Purpose:
#   Simple text-based menu program that allows the user to
#   append text to a buffer, clear it, display it, or exit.
# Resources: Written by student after class lectures.

# start with an empty buffer
buffer = ""

# variable to store the user's menu choice
choice = ""

# keep showing menu until the user chooses option 4
while choice != "4":
    print("\n--- Menu ---")
    print("1. Append to buffer")
    print("2. Clear buffer")
    print("3. Display buffer")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        # add text to the buffer
        text = input("Enter text: ")
        buffer = buffer + text
    elif choice == "2":
        # clear the buffer
        buffer = ""
    elif choice == "3":
        # show current contents of the buffer
        print("Buffer:", buffer)
    elif choice == "4":
        # end program
        print("Goodbye!")
