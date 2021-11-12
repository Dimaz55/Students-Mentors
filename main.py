def average_grade(grades):
    pass
    return 'оценок пока нет' if not grades else 'средняя оценка'


class Student:
    def __init__(self, name, surname, gender):
        self._name = name
        self._surname = surname
        self._gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress) or 'отсутствуют'
        finished_courses = ', '.join(self.finished_courses) or 'отсутствуют'
        info_card = f'Имя: {self._name}\n'\
                    f'Фамилия: {self._surname}\n'\
                    f'Средняя оценка за домашние задания: {average_grade(self.grades)}\n'\
                    f'Курсы в процессе изучения: {courses_in_progress}\n'\
                    f'Завершенные курсы: {finished_courses}\n'
        return info_card


class Mentor:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


if __name__ == '__main__':

    student_0 = Student('Иван', 'Петров', 'муж.')
    student_0.courses_in_progress += ['Python']
    student_0.finished_courses += ['HTML']

    student_1 = Student('Елена', 'Головач', 'жен.')
    student_1.courses_in_progress += ['GIT']

    student_list = [student_0, student_1]

    mentor_0 = Mentor('Козьма', 'Прутков')
    mentor_0.courses_attached += ['Python']

    mentor_0.rate_hw(student_0, 'Python', 10)
    mentor_0.rate_hw(student_0, 'Python', 8)
    mentor_0.rate_hw(student_1, 'Python', 10)

    print(student_0)
    print(student_1)
