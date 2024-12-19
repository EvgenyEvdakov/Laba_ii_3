#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Генерация списка возможных слов из матрицы символов

def find_words(board, dictionary):
    found_words = set()
    rows, cols = len(board), len(board[0])

    # Направления для перемещения (восемь направлений)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),        (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    # Рекурсивная функция для поиска слов
    def dfs(x, y, path, visited):
        path += board[x][y]  # Добавляем текущий символ к пути
        if path in dictionary:
            found_words.add(path)  # Если слово найдено, добавляем его в набор

        if len(path) > max_length:
            return

        # Проверка всех направлений
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < rows and
                0 <= new_y < cols and
                (new_x, new_y) not in visited):
                visited.add((new_x, new_y))  # Добавляем в посещенные
                dfs(new_x, new_y, path, visited)
                visited.remove((new_x, new_y))  # Убираем из посещенных

    max_length = max(len(word) for word in dictionary)  # Длина самого длинного слова

    # Ищем слова, начиная с каждой клетки
    for i in range(rows):
        for j in range(cols):
            visited = set()
            visited.add((i, j))  # Начинаем с текущей ячейки
            dfs(i, j, '', visited)  # Запускаем поиск

    return found_words

if __name__ == '__main__':
    # Матрица букв
    board = [
        ['Р', 'А', 'С'],
        ['Т', 'Е', 'Л'],
        ['И', 'О', 'Н']
    ]

    # Словарь возможных слов для поиска
    dictionary = ['ЛЕС', 'ТОН', 'НОС', 'РОСТ', 'СТОЛ', 'СЛОН', 'НОТА', 'СОН', 'САЛОН', 'ТАНЦОР']

    # Вызов функции find_words
    result = find_words(board, dictionary)
    print("Найденные слова:", result)