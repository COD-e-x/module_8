from task_1 import Teacher


class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_teacher_data(self):
        return f'{super().get_teacher_data()}\nПредмет {self.__discipline}, должность {self.__job_title}'

    def add_mark(self, name_student, grade):
        return f'{super().add_mark(name_student, grade)}\nПредмет: {self.get_discipline()}'

    def remove_mark(self, name_student, grade):
        return f'{super().remove_mark(name_student, grade)}\nПредмет: {self.get_discipline()}'

    def give_a_consultation(self, classroom):
        return (
            f'{super().give_a_consultation(classroom)}\nПо предмету {self.__discipline} как {self.__job_title}'
        )


if __name__ == '__main__':
    discipline_teacher = DisciplineTeacher('Иван Петров', 'БГПУ', 4, 'Химия', 'Директор')
    print(discipline_teacher.get_teacher_data())
    print(discipline_teacher.add_mark('Николай Иванов', 4))
    print(discipline_teacher.remove_mark('Дмитрий Сидоров', 3))
    print(discipline_teacher.give_a_consultation('10 Б'))
    print()

    discipline_teacher.set_job_title('Преподаватель')
    print(discipline_teacher.get_teacher_data())