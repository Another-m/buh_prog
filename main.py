from datetime import datetime
from application import salary, people

class main():
    def __init__(self, user):
        self.user = user

    def calling_other_functions(self):
        self.data_today()
        salary.calculate_salary()
        people.get_employees()

    def data_today(self):
        print(f"Сегодня: {datetime.today().replace(microsecond=0)}")
        print("Имя пользователя: {}\n".format(self.user))



if __name__ == "__main__":
    admin = main("administrator")
    admin.calling_other_functions()
