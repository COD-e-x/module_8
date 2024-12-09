class Teacher:
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience

    def get_teacher_data(self):
        return f'{self.get_name()}, образование {self.get_education()}, опыт работы {self.get_experience()} года.'

    def add_mark(self, name_student, grade):
        return f'{self.get_name()} поставил оценку {grade} студенту {name_student}.'

    def remove_mark(self, name_student, grade):
        return f'{self.get_name()} удалил оценку {grade} студенту {name_student}.'

    def give_a_consultation(self, classroom):
        return f'{self.get_name()} провел консультацию в классе {classroom}.'


if __name__ == '__main__':
    teacher = Teacher('Иван Петров', 'БГПУ', 4)
    print(teacher.get_teacher_data())
    print(teacher.add_mark('Петр Сидоров', 4))
    print(teacher.remove_mark('Дмитрий Степанов', 3))
    print(teacher.give_a_consultation('9Б'))
    print()

    teacher.set_experience(5)
    print(teacher.get_teacher_data())
