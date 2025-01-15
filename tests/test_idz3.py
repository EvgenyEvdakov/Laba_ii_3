#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest


sys.path.append("../src")
from idz3 import Node, Problem, depth_first_recursive_search


class TestGraphSearch(unittest.TestCase):
    def setUp(self):
        # Определяем граф в виде списка смежности
        self.graph = {
            1: [(2, 43), (4, 140)],
            2: [(1, 43), (3, 35)],
            3: [(2, 35), (4, 68)],
            4: [(1, 140), (3, 68), (5, 96)],
            5: [(4, 96)],
        }

    def test_shortest_path(self):
        # Тестируем поиск кратчайшего пути
        problem = Problem(1, 5)
        path, distance = depth_first_recursive_search(problem, self.graph)
        self.assertEqual(path, [1, 4, 5])
        self.assertEqual(distance, 236)

    def test_no_path(self):
        # Тестируем случай, когда пути нет
        problem = Problem(1, 10)  # Узел 10 отсутствует
        path, distance = depth_first_recursive_search(problem, self.graph)
        self.assertIsNone(path)
        self.assertEqual(distance, float("inf"))

    def test_same_start_and_goal(self):
        # Тестируем случай, когда начальный и конечный узлы совпадают
        problem = Problem(1, 1)
        path, distance = depth_first_recursive_search(problem, self.graph)
        self.assertEqual(path, [1])
        self.assertEqual(distance, 0)


if __name__ == "__main__":
    unittest.main()
