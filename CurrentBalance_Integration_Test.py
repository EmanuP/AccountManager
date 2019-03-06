import sqlite3

from Dummy_DB import create_dummy, delete_dummy

import unittest
from unittest import TestCase

import CurrentBalance

conn = create_dummy("./test.db")

class TestBalanceMethods(TestCase):

    def test_balance_when_existing(self):
        self.assertEqual(CurrentBalance.check_account_balance(conn, 'EmanueleP'), 1.2)

    def test_balance_existence_when_non_existing(self):   
        self.assertEqual(CurrentBalance.check_account_balance(conn, 'PincoP'), None)

    def tearDownClass():
        conn.close()
        delete_dummy("./test.db")


if __name__ == '__main__':
    unittest.main()
