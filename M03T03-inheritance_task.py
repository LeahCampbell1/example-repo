class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # Method to display head office location
    def head_office_location(self):
        print("Cape Town")

# Creates new subclass ofclass "Course" inheriting its attributes
class OOPCourse(Course):

    # Creates variables with default attributes
    description = "OOP Fundamentals"
    trainer = "Mr Anon A. Mouse"

    # Defines method to output trainer and description in string
    def trainer_details(self):
        print("The trainer is ", self.trainer," and the course is about ",self.description)

    # Defines method to output course ID
    def show_course_id(self):
        print("The course ID is #12345")

# Creates object of class
course_1 = OOPCourse()

# Calls class methods
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()



# # Example usage:
# # Create an instance of the Course class
# course = Course()

# # Call the contact_details method to display contact information
# course.contact_details()
