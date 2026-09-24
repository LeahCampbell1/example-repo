"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email:

# Initialise the instance variables for each email.
    has_been_read = False
    def __init__(self, email_address, Subject_line, email_content):
        self.email_address = email_address
        self.Subject_line = Subject_line
        self.email_content = email_content


# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.
    def mark_as_read(self):
        self.has_been_read = True

    # def __str__(self):
    #     return f"{self.email_address}, {self.Subject_line}, {self.email_content}"


# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    emails = [Email("Supermarket_marketing@gmail.com",
                    "You've got points",
                    "Log into your account to retrieve your spending points"), 
            Email("car_dealership@gmail.com",
                  "MOT due soon", 
                  "Please contact our service department to arrange your MOT"), 
            Email("job_recruiter@gmail.com",
                  "Vacancy available",
                  "Hello we would like to set up a call regarding a vacany which matches your credentials"),
                  ]
    inbox.extend(emails)


def list_emails():
    # Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    for index_num, email in enumerate(inbox):
        print(f"{index_num}. {email.Subject_line}")


def read_email(index):
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    if index >= 0 and index <= len(inbox):
        email = inbox[index]
        print("Heres the details of your selected email")
        print(f"Sender: {email.email_address}")
        print(f"Subject: {email.Subject_line}")
        print(f"Content: {email.email_content}")
        if not email.has_been_read:
            email.mark_as_read()
            print(f"Email from {email.email_address} has been read")
    else:
        print("Number not recognised")


def view_unread_emails():
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    for index, email  in enumerate(inbox):
        if not email.has_been_read:
            print(f"Emails with subject {index}. {email.Subject_line}")


# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
inbox = []
# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
populate_inbox()
# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # Add logic here to read an email
        list_emails()
        index = int(input("Enter the value of the email you want to read"))
        read_email(index)


    elif user_choice == 2:
        # Add logic here to view unread emails
        view_unread_emails()

    elif user_choice == 3:
        # Add logic here to quit application.
        break

    else:
        print("Oops - incorrect input.")
