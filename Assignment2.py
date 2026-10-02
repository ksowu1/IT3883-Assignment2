


# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Komi Sowu
# Assignment Number: Lab 1
# Due Date: 10/02/2026
# Purpose: This program reads student names and six grades from an input file.
#          It calculates each student's final average, sorts the students from
#          highest to lowest average, and displays the results.
# Resources Used: Course materials, Python documentation, and class notes.

def process_student_grades():

    # Ask the user for the name of the input file
    filename = input("Enter the input file name: ")

    # Create an empty list to store student information
    students = []

    # Open and read the input file
    with open(filename, "r") as file:

        # Process each student one line at a time
        for line in file:

            # Remove extra spaces and skip empty lines
            line = line.strip()

            if not line:
                continue

            # Split the student's name and scores
            parts = line.split()

            # First item is the student's name
            name = parts[0]

            # Convert the six scores from strings to numbers
            scores = [float(score) for score in parts[1:]]

            # Calculate the student's average
            average = sum(scores) / len(scores)

            # Store the student's name and average
            students.append((name, average))

    # Sort students by average from highest to lowest
    students.sort(key=lambda student: student[1], reverse=True)

    # Display the final results
    print("\nFinal Grades")
    print("--------------------")

    for name, average in students:
        print(f"{name} {average:.2f}")


# Start the program
if __name__ == "__main__":
    process_student_grades()
