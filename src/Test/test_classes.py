import random
import sqlite3

class Herd:
    def __init__(self):
        self.len_ind = 10
        self.quantity = 1231123
        self.individuals = []
        self.con = sqlite3.connect('test-db.sqlite3')
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



ex = Herd()
ex.generate_animals()