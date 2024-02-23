class Grades():
    def __init__(self):
        self.grades = {}
    
    def add_subjects(self):
        number_subjects = int(input("Type the number of subjects: "))
        while number_subjects != 0:
            name = input("Type the name of the subject: ")
            self.grades[name] = ""
            print("Succesfull registration!")
            number_subjects -= 1
    
    def add_grades(self):
        print("List of subjects: ")
        for k in self.grades.keys():
            print(f"-{k}")
        search_subject = input("Type the name of the subject: ")
        if search_subject in self.grades:
            number_students = int(input("Type the number of students: "))
            for i in range(number_students):
                student = input("Type the name of the student: ")
                grade = float(input("Type the grade of the student: "))
                self.grades[search_subject] = { student : grade }
                print("Grades added succesfully")
        else: 
            print("Subject not found!")


    def show_grades(self):
        print("List of subjects: ")
        for k in self.grades.keys():
            print(f"-{k}")
        search_subject = input("Type the name of the subject: ")
        if search_subject in self.grades:
            print(f"{search_subject}: ")
            for student, grade in self.grades[search_subject].items():
                print(f"{student} : {grade}")
        else: 
            print("Subject not found")
            


grade1 = Grades()
grade1.add_subjects()
grade1.add_grades()
grade1.add_grades()
grade1.show_grades()
        
