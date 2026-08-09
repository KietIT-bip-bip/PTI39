from B3_4.models.subjects import SubjectList
class Student:
    def __init__(self, name, student_id,birth_date, subjects_list,password):
        self.name = name
        self.student_id = student_id
        self.birth_date = birth_date
        self.subjects_list = subjects_list
        self.password = password

    def __str__(self):
        return f"""
        Student: {self.name},
        Student ID: {self.student_id},
        Birth Date: {self.birth_date},
        Subjects List: {self.subjects_list}
        """
    #getter
    def get_student_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def get_birth_date(self):
        return self.birth_date

    def get_subjects_list(self):
        return self.subjects_list

    #setter
    def set_student_id(self, student_id):
        if student_id and len(student_id) == 8: self.student_id = student_id
        else: raise ValueError("Student ID must be 8 characters long")

    def set_name(self, name):
        if name: self.name = name
        else: raise ValueError("Name cannot be empty")

    def set_birth_date(self, birth_date):
        #check string format of birth_date dd/mm/yyyy
        if len(birth_date) == 10 and birth_date[2] == '/' and birth_date[5] == '/':
            #check if the day, month, year are valid numbers
            self.birth_date = birth_date
            day = birth_date[0:2]
            month = birth_date[3:5]
            year = birth_date[6:10]
            if len(year) == 4 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                self.birth_date = birth_date
            else: raise ValueError("Invalid date format. Please use dd/mm/yyyy")

    def set_subjects_list(self, subjects_list:SubjectList):
        self.subjects_list = subjects_list

    #------------------
    def get_GPA(self):
        # cp1: 25%, cp2: 25%, final_exam: 50%
        pass

    