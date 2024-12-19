#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from idz2 import find_words


class TestFindWords(unittest.TestCase):
    def setUp(self):
        # Устанавливаем тестовые данные
        self.board = [
            ['Р', 'А', 'С'],
            ['Т', 'Е', 'Л'],
            ['И', 'О', 'Н']
        ]
        self.dictionary = ['ЛЕС', 'ТОН', 'НОС', 'СОН', 'РОСТ']

    def test_no_matching_words(self):
        # Проверяем случай, когда нет совпадений
        result = find_words(self.board, ['МОРЕ', 'ГОРЫ'])
        self.assertEqual(result, set())

    def test_single_letter_word(self):
        # Проверяем, когда словарь содержит односимвольное слово
        board = [['А']]
        dictionary = ['А', 'Б']
        result = find_words(board, dictionary)
        self.assertEqual(result, {'А'})

if __name__ == "__main__":
    unittest.main()