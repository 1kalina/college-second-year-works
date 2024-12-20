import numpy as np

# Введення кількості рядків та стовпців
columns = int(input("Кількість стовпців: "))
rows = int(input("Кількість рядків: "))


# Функція для введення елементів у матрицю
def elements():
    matrix = []
    for i in range(rows):  # рядки
        row = []
        for j in range(columns):  # стовпці
            num = float(input(f"Введіть елемент №{j + 1} рядка {i + 1}: "))
            row.append(num)

        if i == rows - 1:
            print()
        else:
            print("Рядок", i + 2)

        matrix.append(row)

    return np.array(matrix)


# Функція для знаходження мінору
def minor(matrix, row, col):
    # Створіть підматрицю, видаливши вказаний рядок і стовпець
    submatrix = np.delete(np.delete(matrix, row, axis=0), col, axis=1)
    # Обчислити визначник підматриці
    return np.linalg.det(submatrix)


# Отримання матриці від користувача
matrix = elements()

# Введення координат для обчислення мінору
row_index = int(input("Введіть номер рядка для мінору: "))
col_index = int(input("Введіть номер стовпця для мінору: "))

print()
# Функція для знахоження рангу
rank = np.linalg.matrix_rank(matrix)
print("Ранг:", rank)

# Обчислення та вивід мінору
basic_minor = minor(matrix, row_index - 1, col_index - 1)
print(f"Основний мінор елемента ({row_index}, {col_index}):", basic_minor)
