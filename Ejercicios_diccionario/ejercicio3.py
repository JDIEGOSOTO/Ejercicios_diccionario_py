class DicStudents():
    def __init__(self):
        self.dic_students = {}
        self.students = {}

    def agregar_estudiante(self):
        student_code = len(self.dic_students) + 1
        nombre = input("Type the name of the student: ")
        self.students["name"] = nombre
        edad = int(input("Type the age of the student: "))
        self.students["age"] = edad
        nota = float(input("Type the GPA of the student: "))
        self.students["GPA"] = nota

        self.dic_students[student_code] = self.students["name"], self.students["age"], self.students["GPA"]


    def show_students(self):
        for k, v in self.dic_students.items():
            print(f"{k} : {v}")


student1 = DicStudents()

student1.agregar_estudiante()
student1.show_students()