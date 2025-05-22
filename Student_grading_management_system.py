def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Make sure the value is  between 0 and 100.")
        except ValueError:
            print("Kindly enter a numeric value.")
#in calculating or grading the mark of the student
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
#the subjects that are to be graded
subjects = ["Math", "Science", "English", "History", "Art"]
marks_dict = {}


for subject in subjects:
    marks_dict[subject] = get_valid_marks(subject)

#in calculating the average marks of the subjects
average_marks = sum(marks_dict.values()) / len(subjects)

# in calculating the grades of the average marks
grade = calculate_grade(average_marks)

# The table of the grading of the subjects
print("\n+-----------+--------+")
print("| Subject   | Marks  |")
print("+-----------+--------+")
for subject, mark in marks_dict.items():
    print(f"| {subject:<9} | {int(mark):<6} |")
print("+-----------+--------+")
print(f"Average: {average_marks:.1f} | Grade: {grade}")