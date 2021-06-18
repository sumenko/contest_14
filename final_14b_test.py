import unittest
from io import StringIO
from random import randint
from typing import Callable, List
from unittest import TestCase
from unittest.mock import patch

from final_14b import QuickSort, gte, lte, main
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
        q = QuickSort()
        with self.subTest(gte=gte, lte=lte):
            for n, test in enumerate(tests):
                print('Test #', n)
                q.sort(test)
                try:
                    srt = sorted(test)
                    self.assertEqual(test, srt)
                except AssertionError:
                    print(*test, '!=', *srt)

    def test_gte(self):
        alla = ('alla', 4, 100)
        gena = ('gena', 6, 1000)
        gosha = ('gosha', 2, 90)
        rita = ('rita', 2, 90)
        timofey = ('timofey', 4, 80)

        self.assertTrue(gte(gena, alla))
        self.assertTrue(gte(timofey, alla))
        self.assertTrue(gte(gosha, rita))
        self.assertTrue(gte(timofey, gosha))

    def test_lte(self):
        alla = ('alla', 4, 100)
        gena = ('gena', 6, 1000)
        gosha = ('gosha', 2, 90)
        rita = ('rita', 2, 90)
        timofey = ('timofey', 4, 80)

        self.assertFalse(lte(gena, alla))
        self.assertFalse(lte(timofey, alla))
        self.assertFalse(lte(gosha, rita))
        self.assertFalse(lte(timofey, gosha))

    def test_sort_with_lte(self):
        test = [
            ('alla', 4, 100),
            ('gena', 6, 1000),
            ('gosha', 2, 90),
            ('rita', 2, 90),
            ('timofey', 4, 80),
        ]
        q = QuickSort(gte, lte, reverse=True)
        q.sort(test)
        answer = [t[0] for t in test]
        self.assertEqual(answer, ['gena', 'timofey', 'alla', 'gosha', 'rita'])

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
