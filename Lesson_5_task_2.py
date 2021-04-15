import datetime


class DisplayedErrors(Exception):
    """Класс ошибок, нужен для выведения наших ошибок"""

    def __str__(self):
        return f'Класс с ошибками'


class Person:
    """Класс Персона"""

    def __init__(self, full_name, born_date=None):
        self.full_name = self.check_full_name(full_name)
        self.born_date = self.check_born_date(born_date)

    def __str__(self):
        return f'{self.full_name} - {self.born_date}'

    def check_full_name(self, full_name):
        """Метод проверяет правильность заполнения поля Имя и фамилия. В случае неправильного ввода возвращает ошибку"""
        if len(full_name.split()) == 2:
            return full_name
        else:
            raise DisplayedErrors(f'\n{"=" * 50}\n|| Вы должны передавать два слова: Имя и фамилию.||\n{"=" * 50}')

    def check_born_date(self, born_date):
        """Метод проверяет правильность заполнения поля Дня рождения. В случае если год больше 2021 или меньше 1900
        возвращает ошибку """
        now = datetime.datetime.now()
        if born_date > now.year:
            raise DisplayedErrors(f'\n{"=" * 50}\n||        Сожелеем но Вы еще не рождены.        ||\n{"=" * 50}')
        elif born_date < 1900:
            raise DisplayedErrors(
                f'\n{"=" * 65}\n||  Проверьте дату своего рождения она должна быть позже 1900  ||\n{"=" * 65}')
        else:
            return born_date

    def only_name(self):
        """Метод выводит только Имя"""
        return self.full_name.split()[0]

    def surname(self):
        """Метод выводит только Фамилию"""
        return self.full_name.split()[0]

    def how_old(self, date=2021):
        """Метод выводит сколько лет будет в конкретном году."""
        return date - self.born_date


class Employee(Person):
    """Класс сотрудник"""

    def __init__(self, full_name, born_date, position, work_experience, salary):
        super().__init__(full_name, born_date)
        self.position = position
        self.work_experience = self.check_work_experience(work_experience)
        self.salary = self.check_salary(salary)

    def __str__(self):
        return f'{self.full_name} - {self.position} - {self.salary}'

    def check_work_experience(self, work_experience):
        """Метод проверяет  правильность заполнения поля рабочий опыт. В случае отрицательного значения возвращает
        ошибку """
        if work_experience < 0:
            raise DisplayedErrors(
                f'\n{"=" * 60}\n|| Опыт может быть нулевым, но не может быть отрицательным ||\n{"=" * 60}')
        else:
            return work_experience

    def check_salary(self, salary):
        """Метод проверяет правильность заполнения поля ЗП. В случае отрицательного значения возвращает ошибку"""
        if salary < 0:
            raise DisplayedErrors(
                f'\n{"=" * 75}\n||   Мы Вам платим, а не Вы нам! Введите зарплату равну или больше нуля. ||\n{"=" * 75}')
        else:
            return salary

    def position_and_level(self):
        """Метод выводить уровень и позицию сотрудника опираясь на введеные данные и опыт работы"""
        if self.work_experience < 3:
            level = 'Junior'
        elif 6 > self.work_experience >= 3:
            level = 'Middle'
        elif self.work_experience >= 6:
            level = 'Senior'
        return f'{level} {self.position}'

    def salary_up(self, bonus):
        """Метод увеличивает значение ЗП на введеное пользователем значение."""
        self.salary += bonus


class ITEmployee(Employee):
    """Класс ИТ-сотрудник"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = []

    def new_skill(self, skill):
        """Метод добавляет один Скил"""
        self.skills.append(skill)

    def new_skills(self, *args):
        """Метод добавляет несколько скилов"""
        self.skills.extend(args)
