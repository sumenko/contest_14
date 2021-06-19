import unittest
from io import StringIO
from random import randint
from typing import Callable, List
from unittest import TestCase
from unittest.mock import patch

from final_14b import Member, main, sort
from final_14b_test_data import tests as test_data


class TestQuickSort(TestCase):
    def test_quick_sort(self):
        tests = (
            [4, 8, 9, 20, 1, 5, 3, 10],
            [1, 2, 0, 4, 5],
            [1, 2, 3, 4, 5],
            [0, 2, 3, 4, 5],
            [1, 0, 3, 4, 5],
            [1, 2, 3, 0, 5],
            [1, 2, 3, 4, 0],
            [randint(0, 10) for _ in range(10)],
        )

        with self.subTest():
            for test in tests:
                srt = sorted(test)
                sort(test)
                try:
                    self.assertEqual(test, srt)
                except AssertionError:
                    print(*test, '!=', *srt)

    def test_lt(self):
        alla = Member('alla', 4, 100)
        gena = Member('gena', 6, 1000)
        gosha = Member('gosha', 2, 90)
        rita = Member('rita', 2, 90)
        timofey = Member('timofey', 4, 80)

        self.assertTrue(gena > alla)
        self.assertFalse(gena < alla)
        self.assertTrue(rita < gosha)
        self.assertTrue(gosha < timofey)

    def test_sort_break_cases(self):
        tests = ([1, 1, 1, 1, 1, 1],
                 [1, 2, 1, 1, 1, 1],
                 [2, 2, 1, 1],
                 [1, 1, 2, 2])
        with self.subTest(msg='strange arrays test'):
            for test in tests:
                srt = sorted(test)
                sort(test)
                try:
                    self.assertEqual(test, srt)
                except AssertionError:
                    print(test, ' != ', srt)

    def _get_output(self,
                    subtest_name: str,
                    module: str,
                    side_effect: List[str],
                    test_func: Callable,
                    ) -> str:
        with self.subTest(
            name=subtest_name,
        ), patch(
            f'{module}.input',
            side_effect=side_effect
        ), patch(
            'sys.stdout', new=StringIO()
        ) as fake_out:
            test_func()
            return fake_out.getvalue()

    def test_main(self):
        for name, data, result in test_data:
            output = self._get_output(name,
                                      'final_14b',
                                      data.split('\n'),
                                      main)
            self.assertEqual(output, result)


if __name__ == '__main__':
    unittest.main()
