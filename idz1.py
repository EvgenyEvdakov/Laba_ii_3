#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Необходимо для задачи "Поиск самого длинного пути в
# матрице" подготовить собственную матрицу, для которой с помощью
# разработанной в предыдущем пункте программы, подсчитать самый длинный
# путь.

def longest_path(matrix, start_char):
    rows = len(matrix)
    cols = len(matrix[0])

    # Возможные направления перемещения (восемь направлений)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),        (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    memo = {}

    def dfs(x, y, prev_char):
        if (x, y) in memo:
            return memo[(x, y)]

        max_length = 1

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < rows and 0 <= new_y < cols and
                    ord(matrix[new_x][new_y]) == ord(prev_char) + 1):
                max_length = max(max_length, 1 + dfs(new_x, new_y, matrix[new_x][new_y]))

        memo[(x, y)] = max_length
        return max_length

    longest = 0

    # Поиск начального символа и запуск DFS
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == start_char:
                longest = max(longest, dfs(i, j, start_char))

    return longest

if __name__ == "__main__":
    # Новая матрица
    new_matrix = [
        ["A", "B", "C", "D", "E", "F", "T"],
        ["Z", "Y", "X", "W", "V", "G", "H"],
        ["I", "J", "K", "L", "M", "T", "S"],
        ["R", "Q", "P", "O", "N", "U", "T"],
        ["S", "T", "U", "V", "W", "X", "Y"],
        ["Z", "A", "B", "C", "D", "E", "F"],
        ["G", "H", "I", "J", "K", "L", "M"]
    ]
    start_char = 'M'

    # Подсчет самого длинного пути
    longest_path_length = longest_path(new_matrix, start_char)

    print("Длина самого длинного пути:", longest_path_length)