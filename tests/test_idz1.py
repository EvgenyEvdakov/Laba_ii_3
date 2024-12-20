#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append('../src')
from idz1 import longest_path


class TestLongestPath(unittest.TestCase):
    def setUp(self):
        # Тестовая матрица
        self.matrix = [
            ["A", "B", "C", "D", "E", "F", "T"],
            ["Z", "Y", "X", "W", "V", "G", "H"],
            ["I", "J", "K", "L", "M", "T", "S"],
            ["R", "Q", "P", "O", "N", "U", "T"],
            ["S", "T", "U", "V", "W", "X", "Y"],
            ["Z", "A", "B", "C", "D", "E", "F"],
            ["G", "H", "I", "J", "K", "L", "M"]
        ]

    def test_longest_path_from_T(self):
        # Проверяем путь, начиная с символа 'T'
        result = longest_path(self.matrix, "T")
        self.assertEqual(result, 6)  # Ожидаемая длина пути

    def test_no_path_starting_char(self):
        # Проверяем случай, когда символа нет в матрице
        result = longest_path(self.matrix, "Z")
        self.assertEqual(result, 1)  # Нет пути, кроме начального узла

    def test_invalid_character(self):
        # Проверяем случай с символом, отсутствующим в матрице
        result = longest_path(self.matrix, "!")
        self.assertEqual(result, 0)  # Нет такого пути


if __name__ == "__main__":
    unittest.main()
