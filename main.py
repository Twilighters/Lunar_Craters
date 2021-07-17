# # Тут будет Ваше исполнение ДЗ


def calculate(my_input: list) -> int:
    """Расчитывает количество лунных кратеров."""
    row = len(my_input)
    col = len(my_input[0])
    count = 0

    for i in range(row):
        for j in range(col):
            if my_input[i][j] == 1:
                passing_deep(my_input, row, col, i, j)
                count += 1
    return count


def passing_deep(my_input: list, row: int, col: int, x: int, y: int) -> None:
    """Проверяет каждый элемент и проходит по матрице."""
    if my_input[x][y] == 0:
        return None
    my_input[x][y] = 0

    if x != 0:
        passing_deep(my_input, row, col, x - 1, y)
    if x != row - 1:
        passing_deep(my_input, row, col, x + 1, y)
    if y != 0:
        passing_deep(my_input, row, col, x, y - 1)
    if y != col - 1:
        passing_deep(my_input, row, col, x, y + 1)
