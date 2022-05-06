import pandas as pd


class AdmittedStudents:
    def __init__(self, csv_file=None, students_id_list=None) -> None:
        if csv_file:
            self.admitted_students = pd.read_csv(csv_file, index_col=0)
        else:
            raise TypeError('Expected .csv file')

    def add_student(self, student_id, student_firstname, student_lastname):
        if student_id not in self.admitted_students.index:
            new_student = [(student_firstname, student_lastname)]
            new_record = pd.DataFrame(new_student, columns=self.admitted_students.columns, index=[student_id])
            self.admitted_students = pd.concat([self.admitted_students, new_record], ignore_index=False)
        else:
            raise KeyError(f'Student with ID {student_id} already exists')

    def delete_student(self, student_id):
        if student_id in self.admitted_students.index:
            self.admitted_students = self.admitted_students.drop([student_id])
        else:
            raise KeyError(f'Student with ID {student_id} does not exist')

    def validate_student(self, student_id):
        if student_id in self.admitted_students.index:
            return 1
        else:
            return 0

    def export_students_to_csv(self, new_filename):
        self.admitted_students.to_csv(new_filename)

