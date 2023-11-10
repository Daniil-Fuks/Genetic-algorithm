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
        for number in range(self.quantity):
            for i in range(self.len_ind):
                num = random.randint(0, 1)
                animal += str(num)
            self.individuals.append([animal, animal.count('1')])
            self.cur.execute(f"INSERT INTO herd(body, force, number_herd) VALUES ('{animal}', {animal.count('1')},\
             1)").fetchall()
            animal = ''
        self.con.commit()

    def get_middle_value(self, num):
        try:
            middle = []
            res = self.cur.execute(f'SELECT * FROM herd WHERE number_herd = {num}').fetchall()
            for item in res:
                middle.append(item[2])
            return sum(middle) / len(middle)

        except ZeroDivisionError:
            return 'Не найдено.'

    def fight(self):
        print('сработала')
        for _ in range(self.quantity):
            id1 = random.randint(1, self.quantity)
            id2 = random.randint(1, self.quantity)

            while id1 == id2:
                id2 = random.randint(1, self.quantity)

            force1 = int(self.cur.execute(f'SELECT force FROM herd WHERE id = {id1}').fetchall()[0][0])
            body1 = self.cur.execute(f'SELECT body FROM herd WHERE id = {id1}').fetchall()[0][0]

            force2 = int(self.cur.execute(f'SELECT force FROM herd WHERE id = {id2}').fetchall()[0][0])
            body2 = self.cur.execute(f'SELECT body FROM herd WHERE id = {id2}').fetchall()[0][0]

            if force1 == force2:
                self.cur.execute(
                    f"INSERT INTO herd(body, force, number_herd) VALUES('{body1}', {force1}, 2)")

            if force1 > force2:
                self.cur.execute(
                    f"INSERT INTO herd(body, force, number_herd) VALUES('{body1}', {force1}, 2)")

            elif force2 > force1:
                self.cur.execute(
                    f"INSERT INTO herd(body, force, number_herd) VALUES('{body2}', {force2}, 2)")
            self.con.commit()

    def reproduction(self):
        # Выбираем два рандомных id. Сначала выбирается число от 1 до количества особей, а затем к нему прибавляется
        # само количество особей, т.к. это вторая версия нашего стада.
        for _ in range(self.quantity):
            id1 = random.randint(1, self.quantity) + self.quantity
            id2 = random.randint(1, self.quantity) + self.quantity

            while id1 == id2:
                id2 = random.randint(1, self.quantity) + self.quantity

            body1 = self.cur.execute(f'SELECT body FROM herd WHERE id = {id1}').fetchall()[0][0]
            body2 = self.cur.execute(f'SELECT body FROM herd WHERE id = {id2}').fetchall()[0][0]

            split = random.randint(1, self.len_ind - 1)
            child = body1[:split] + body2[split:]
            force = child.count('1')
            self.cur.execute(f"INSERT INTO herd(body, force, number_herd) VALUES('{child}', {force}, 3)")
            self.con.commit()

    def mutation(self, prob):
        for i in range(self.quantity):
            id_ind = i + self.quantity * 2 + 1
            body = self.cur.execute(f'SELECT body FROM herd WHERE id = {id_ind}').fetchall()[0][0]
            ind = ''
            for i in range(len(body)):
                flag = random.randint(1, 100)
                if prob >= flag:
                    if body[i] == '1':
                        ind += '0'
                    elif body[i] == '0':
                        ind += '1'
                else:
                    ind += body[i]
            print(ind, id_ind)
