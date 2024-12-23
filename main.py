def is_eligible_for_class(age):
    """
    Checks if a student is eligible to enroll in Raj's class based on their age.

    Args:
        age: The age of the student.

    Returns:
        True if the student is eligible, False otherwise.
    """

    if 10 <= age <= 20:
        return True
    else:
        return False

# Get the age of the student from the user
age = int(input("Enter your age: "))

# Check if the student is eligible for the class
if is_eligible_for_class(age):
    print("You are eligible to enroll in Raj's class.")
else:
    print("You are not eligible to enroll in Raj's class.")