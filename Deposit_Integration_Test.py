import sqlite3

from Dummy_DB import create_dummy, delete_dummy

import unittest
from unittest import TestCase, mock

import Deposit, CurrentBalance

conn = create_dummy("./test.db")

class TestBalanceMethods(TestCase):

    def test_deposit_when_existing(self):

        self.assertEqual(Deposit.deposit_on_account_balance(conn, 'EmanueleP',1.0), True)
        self.assertEqual(CurrentBalance.check_account_balance(conn, 'EmanueleP'), 2.2)

    def test_deposit_when_not_existing(self):

        self.assertEqual(Deposit.deposit_on_account_balance(conn, 'PincoP',1.0), False)
 
    def test_deposit_when_negative(self):

        self.assertEqual(Deposit.deposit_on_account_balance(conn, 'EmanueleP',-1.0), False)
        self.assertEqual(CurrentBalance.check_account_balance(conn, 'EmanueleP'), 2.2)    

    def tearDownClass():
        conn.close()
        delete_dummy("./test.db")


if __name__ == '__main__':

    unittest.main()

