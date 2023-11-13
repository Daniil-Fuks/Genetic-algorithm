import random
import sqlite3


class Herd:
    def __init__(self):
        self.len_ind = 0
        self.quantity = 0
        self.individuals = []
        self.iteration_number = 0
        self.last_id = 0
        self.con = sqlite3.connect('test-db.sqlite3')
        self.cur = self.con.cursor()
        self.first_iteration = True

    def cleaning(self):
        self.cur.execute(f'DELETE FROM herd WHERE iteration_number = 1')
        self.cur.execute(f'UPDATE herd SET iteration_number = 1')
        self.cur.execute(f'UPDATE herd SET number_herd = 1')
        self.con.commit()

    def set_iteration_number(self, num):
        self.iteration_number = num

    def set_first_iteration_flag(self):
        self.first_iteration = False

    def set_quantity(self, num):
        self.quantity = int(num)

    def set_len_ind(self, num):
        self.len_ind = int(num)

    def get_last_id(self):
        return self.cur.execute(f'SELECT MAX(id) FROM herd').fetchall()[0][0]

    def generate_animals(self):
        # Создание первого стада
        animal = ''
        for number in range(int(self.quantity)):
            for i in range(int(self.len_ind)):
                num = random.randint(0, 1)
                animal += str(num)
            self.individuals.append([animal, animal.count('1')])
            self.cur.execute(
                f"INSERT INTO herd(body, force, number_herd, iteration_number) VALUES ('{animal}', {animal.count('1')}, \
             1, 1)")
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
        for _ in range(self.quantity):
            if self.first_iteration:
                id1 = random.randint(1, self.quantity)
                id2 = random.randint(1, self.quantity)

                while id1 == id2:
                    id2 = random.randint(1, self.quantity)

            else:
                id1 = random.randint(1, self.quantity) + self.last_id - self.quantity
                id2 = random.randint(1, self.quantity) + self.last_id - self.quantity

                while id1 == id2:
                    id2 = random.randint(1, self.quantity) + self.last_id - self.quantity

            force1 = self.cur.execute(f'SELECT force FROM herd WHERE id = {id1}').fetchall()[0][0]
            body1 = self.cur.execute(f'SELECT body FROM herd WHERE id = {id1}').fetchall()[0][0]

            force2 = int(self.cur.execute(f'SELECT force FROM herd WHERE id = {id2}').fetchall()[0][0])
            body2 = self.cur.execute(f'SELECT body FROM herd WHERE id = {id2}').fetchall()[0][0]

            if force1 == force2:
                self.cur.execute(
                    f"INSERT INTO herd(body, force, number_herd, iteration_number) VALUES('{body1}', {force1}, 2, 1)")

            if force1 > force2:
                self.cur.execute(
                    f"INSERT INTO herd(body, force, number_herd, iteration_number) VALUES('{body1}', {force1}, 2, 1)")

            elif force2 > force1:
                self.cur.execute(
                    f"INSERT INTO herd(body, force, number_herd, iteration_number) VALUES('{body2}', {force2}, 2, 1)")
            self.con.commit()

    def reproduction(self):
        # Выбираем два рандомных id. Сначала выбирается число от 1 до количества особей, а затем к нему прибавляется
        # само количество особей, т.к. это вторая версия нашего стада.
        for _ in range(self.quantity):
            id1 = random.randint(1, self.quantity) + self.last_id - 5
            id2 = random.randint(1, self.quantity) + self.last_id - 5

            while id1 == id2:
                id2 = random.randint(1, self.quantity) + self.last_id - 5

            body1 = self.cur.execute(f'SELECT body FROM herd WHERE id = {id1}').fetchall()[0][0]
            body2 = self.cur.execute(f'SELECT body FROM herd WHERE id = {id2}').fetchall()[0][0]

            split = random.randint(1, self.len_ind - 1)
            child = body1[:split] + body2[split:]
            force = child.count('1')
            self.cur.execute(f"INSERT INTO herd(body, force, number_herd, iteration_number) VALUES('{child}', {force}, \
             3, 1)")

            self.con.commit()

    def mutation(self, prob):
        for i in range(self.quantity):
            id_ind = i + self.last_id
            body = self.cur.execute(f'SELECT body FROM herd WHERE id = {id_ind}').fetchall()[0][0]
            ind = ''
            for j in range(len(body)):
                flag = random.randint(1, 100)
                if prob >= flag:
                    if body[j] == '1':
                        ind += '0'
                    elif body[j] == '0':
                        ind += '1'
                else:
                    ind += body[j]
            self.cur.execute(f"INSERT INTO herd(body, force, number_herd, iteration_number) VALUES('{ind}', \
            {ind.count('1')}, 4, 2)")
        self.con.commit()
