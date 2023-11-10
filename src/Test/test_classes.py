import random
import sqlite3


class Herd:
    def __init__(self):
        self.len_ind = 10
        self.quantity = 5
        self.individuals = []
        self.con = sqlite3.connect('test-bd.db')
        self.cur = self.con.cursor()

    def set_quantity(self, num):
        self.quantity = num

    def set_len_ind(self, num):
        self.len_ind = num

    def generate_animals(self):  # Создание первого стада
        animal = ''
        for _ in range(self.quantity):
            for i in range(self.len_ind):
                num = random.randint(0, 1)
                animal += str(num)
            self.individuals.append([animal, animal.count('1')])
            self.cur.execute(f"INSERT INTO herd(body, force) VALUES ('{animal}', {animal.count('1')})").fetchall()
            animal = ''
        self.con.commit()

    def get_middle_value(self):
        middle = []
        for i in range(self.quantity):
            res = self.cur.execute('SELECT * FROM herd').fetchall()
            middle.append(res[i][2])
        return sum(middle) / len(middle)

    def fight(self):
        num1 = random.randint(1, self.quantity)
        num2 = random.randint(1, self.quantity)
        if num1 == num2:
            ...
