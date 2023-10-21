import random


def generate_animals(num):  # Создание одной особи
    animal = ''
    list_parrants = []
    for i in range(num):
        for i in range(5):
            num = random.randint(0, 1)
            animal += str(num)
        list_parrants.append(animal)
        animal = ''
    return list_parrants


#
# def fight():  # Создание битвы
#     num = random.randint(0, 4)
#     num2 = random.randint(0, 4)
#     if num == num2:
#         return animals[num]
#     else:
#         if animals[num][1] > animals[num2][1]:
#             return animals[num]
#         else:
#             return animals[num2]


# def new_child():
#     child_1 = winner[random.randint(0, 4)]
#     child_2 = winner[random.randint(0, 4)]
#
#     split = random.randint(0, 4)
#
#     child = child_1[:split] + child_2[split:]
#     return child

#
# def mutation():
#     for i in range(len(new_children)):
#         child = ''
#         for j in range(len(new_children[i][0])):
#             chanse = random.randint(0, 100)
#             if 0 <= chanse <= 5:
#                 if new_children[i][0][j] == '0':
#                     child += '1'
#                 else:
#                     child += '0'
#             else:
#                 child += str(new_children[i][0][j])
#         mutation_child.append([child, child.count('1')])
#     return mutation_child


animals = []

# for i in range(5):
#     animals.append(generate_animal())
# print("Родители")
# print(animals)
# print()
# print()
#
# winner = []
# while len(winner) != 5:
#     winner.append(fight())
#
# print("После всех драк:")
# print(winner)
# print()
# print()
#
# new_children = []
# for i in range(5):
#     new_children.append(new_child())
#
# print('Новые дети:')
# print(new_children)
#
# mutation_child = []
# print()
# print()
#
# print("Дети после мутации:")
# print(mutation())
