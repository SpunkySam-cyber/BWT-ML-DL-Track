def enter_student_details():
    students = []
    for i in range(3):
        print(f"\nEnter details for student {i+1}:")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = float(input("Enter grade: "))
        students.append((name, age, grade))
    return students

def list_to_dict(students):
    student_dict = {}
    for student in students:
        name, age, grade = student
        student_dict[name] = (age, grade)
    return student_dict

def display_output(student_dict):
    print("\nStudent details:")
    for name, details in student_dict.items():
        age, grade = details
        print(f"Name: {name}, Age: {age}, Grade: {grade}")

def main():

    students = enter_student_details()
    
    student_dict = list_to_dict(students)
    
    display_output(student_dict)

if __name__ == "__main__":
    main()
