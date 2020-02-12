#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        result = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                result[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in result]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in result]))


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[2, 4, 5], [1, 3, 5], [7, 9, 8]])


print(m.__add__())
