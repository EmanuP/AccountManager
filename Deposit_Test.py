import sqlite3

from Dummy_DB import create_dummy, delete_dummy

import unittest
from unittest import TestCase, mock

import Deposit, CurrentBalance

conn = create_dummy("./test.db")

class TestBalanceMethods(TestCase):

    def test_deposit_when_existing(self):

        with mock.patch('Deposit.Login.check_user_existence') as loginMock:
            loginMock.return_value = 512
            with mock.patch('Deposit.CurrentBalance.check_account_balance') as balanceMock:
                balanceMock.return_value = 1.2          

            self.assertEqual(Deposit.deposit_on_account_balance(conn, 'EmanueleP',1.0), True)
    
        self.assertEqual(CurrentBalance.check_account_balance(conn, 'EmanueleP'), 2.2)

    def test_deposit_when_not_existing(self):

        with mock.patch('Deposit.Login.check_user_existence') as loginMock:
            loginMock.return_value = None
            with mock.patch('Deposit.CurrentBalance.check_account_balance') as balanceMock:
                balanceMock.return_value = 1.2          

            self.assertEqual(Deposit.deposit_on_account_balance(conn, 'PincoP',1.0), False)
 
    def test_deposit_when_negative(self):

        with mock.patch('Deposit.Login.check_user_existence') as loginMock:
            loginMock.return_value = 512
            with mock.patch('Deposit.CurrentBalance.check_account_balance') as balanceMock:
                balanceMock.return_value = 2.2          

            self.assertEqual(Deposit.deposit_on_account_balance(conn, 'EmanueleP',-1.0), False)
    
        self.assertEqual(CurrentBalance.check_account_balance(conn, 'EmanueleP'), 2.2)    

    def tearDownClass():
        conn.close()
        delete_dummy("./test.db")


if __name__ == '__main__':

    unittest.main()

