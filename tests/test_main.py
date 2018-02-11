# !/usr/bin/env python3
# coding: utf-8
""" test.py """

import unittest
from hoge import Hoge

class TestMain(unittest.TestCase):
    """ test class """

    def test_put(self):
        """ hoge test """
        hoge = Hoge()
        env = hoge.put()
        self.assertEqual(env, 'test')

if __name__ == "__main__":
    unittest.main()