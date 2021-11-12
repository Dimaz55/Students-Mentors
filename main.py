def average_grade(grades: dict):
    """Подсчёт средней оценки по всем курсам"""
    if grades:
        average_course_grade = []
        for grade_list in grades.values():
            average_course_grade.append(
                    round(sum(grade_list) / len(grade_list), 1)
                                       )
        return sum(average_course_grade) / len(grades)
    else:
        return 'оценок пока нет'


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)\
                              or 'отсутствуют'
        finished_courses = ', '.join(self.finished_courses) or 'отсутствуют'
        info_card = f'Имя: {self.name}\n'\
                    f'Фамилия: {self.surname}\n'\
                    f'Средняя оценка за домашние задания: ' \
                    f'{average_grade(self.grades)}\n'\
                    f'Курсы в процессе изучения: {courses_in_progress}\n'\
                    f'Завершенные курсы: {finished_courses}\n'
        return info_card

    def rate_lecturer(self, lecturer, course, grade):
        """Метод добавляения оценки *grade* для лектора *lecturer*
        по курсу *course*
        """
        if not isinstance(lecturer, Lecturer):
            print("!!! Ошибка: студентам можно оценивать только лекторов.\n")
        elif course not in lecturer.courses_attached:
            print(f"!!! Ошибка: преподаватель {lecturer.name} "
                  f"{lecturer.surname} не ведёт курс у данного студента.\n")
        elif course not in self.courses_in_progress:
            print(f"!!! Ошибка: Данный студент не проходит курс {course}.\n")
        elif type(grade) is str and 10 < grade < 0:
            print(f'!!! Ошибка: оценка должна быть в диапазоне (1-10).\n')
        else:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        info_card = f'Имя: {self.name}\n'\
                    f'Фамилия: {self.surname}\n'\
                    f'Средняя оценка за лекции: '\
                    f'{average_grade(self.grades)}\n'
        return info_card


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        info_card = f'Имя: {self.name}\n'\
                    f'Фамилия: {self.surname}\n'
        return info_card

    def rate_hw(self, student, course, grade: "int, 1:10"):
        """
        Метод добавления оценки *grade* за домашнее задание студента
        *student* по курсу *course*
        """
        if not isinstance(student, Student):
            print("!!! Ошибка: ставить оценки за домашнее задание можно "
                  "только студентам.\n")
        elif course not in self.courses_attached:
            print(f"!!! Ошибка: преподаватель {self.name} {self.surname} "
                  f"не ведёт курс {course}.\n")
        elif course not in student.courses_in_progress:
            print(f"!!! Ошибка: студент {student.name} {student.surname} "
                  f"не обучается на курсе {course}.\n")
        elif grade <= 0 or grade > 10:
            print(f'!!! Ошибка: оценка должна быть в диапазоне от 1 до 10.\n')
        else:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]


if __name__ == '__main__':

    student_0 = Student('Иван', 'Петров',)
    student_0.courses_in_progress += ['Python']
    student_0.finished_courses += ['HTML']

    student_1 = Student('Елена', 'Головач')
    student_1.courses_in_progress += ['GIT']

    reviewer_0 = Reviewer('Козьма', 'Прутков')
    reviewer_0.courses_attached += ['Python']

    reviewer_1 = Reviewer('Фёдор', 'Шаляпин')
    reviewer_1.courses_attached += ['GIT']

    lecturer_0 = Lecturer('Григорий', 'Распутин')
    lecturer_0.courses_attached += ['Python']

    lecturer_1 = Lecturer('Степан', 'Разин')
    lecturer_1.courses_attached += ['GIT']

    # Проверка обработки ошибок
    reviewer_0.rate_hw(student_0, 'Python', 11)  # оценка не в диапазоне 1:10
    reviewer_0.rate_hw(student_0, 'HTML', 5)  # не проверяет курс HTML
    reviewer_1.rate_hw(reviewer_0, 'GIT', 10)  # попытка оценить проверяющего
    student_0.rate_lecturer(reviewer_0, 'Python', 5)  # оценка проверяющего

    # Удачное добавление оценок
    reviewer_0.rate_hw(student_0, 'Python', 10)
    reviewer_0.rate_hw(student_0, 'Python', 8)
    reviewer_0.rate_hw(student_0, 'Python', 3)

    reviewer_1.rate_hw(student_1, 'GIT', 5)
    reviewer_1.rate_hw(student_1, 'GIT', 8)
    reviewer_1.rate_hw(student_1, 'GIT', 9)

    student_0.rate_lecturer(lecturer_0, 'Python', 8)
    student_0.rate_lecturer(lecturer_0, 'Python', 10)
    student_0.rate_lecturer(lecturer_0, 'Python', 10)

    student_1.rate_lecturer(lecturer_1, 'GIT', 1)
    student_1.rate_lecturer(lecturer_1, 'GIT', 10)
    student_1.rate_lecturer(lecturer_1, 'GIT', 8)

    print(student_0)
    print(student_1)

    print(reviewer_0)
    print(reviewer_1)

    print(lecturer_0)
    print(lecturer_1)
