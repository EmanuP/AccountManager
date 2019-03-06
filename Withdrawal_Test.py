import sqlite3

from Dummy_DB import create_dummy, delete_dummy

import unittest
from unittest import TestCase, mock

import Withdrawal,CurrentBalance

conn = create_dummy("./test.db")

class TestBalanceMethods(TestCase):

    def test_withdrawal_when_existing(self):

        with mock.patch('Withdrawal.Login.check_user_password') as loginMock:
            loginMock.return_value = 1
            with mock.patch('Withdrawal.CurrentBalance.check_account_balance') as balanceMock:
                balanceMock.return_value = 1.2          

                self.assertEqual(Withdrawal.withdrawal_on_account_balance(conn, 'EmanueleP', 'abcd1234',1.0), True)
    
        self.assertEqual(CurrentBalance.check_account_balance(conn, 'EmanueleP'), 0.2)

    def test_withdrawal_when_not_existing(self):

        with mock.patch('Withdrawal.Login.check_user_password') as loginMock:
            loginMock.return_value = None
            with mock.patch('Withdrawal.CurrentBalance.check_account_balance') as balanceMock:
                balanceMock.return_value = None          

                self.assertEqual(Withdrawal.withdrawal_on_account_balance(conn, 'EmanueleP', 'abcd1234',1.0), False)
    
        self.assertEqual(CurrentBalance.check_account_balance(conn, 'EmanueleP'), 0.2)

    def test_withdrawal_when_negative(self):

        with mock.patch('Withdrawal.Login.check_user_password') as loginMock:
            loginMock.return_value = None
            with mock.patch('Withdrawal.CurrentBalance.check_account_balance') as balanceMock:
                balanceMock.return_value = None          

                self.assertEqual(Withdrawal.withdrawal_on_account_balance(conn, 'EmanueleP', 'abcd1234', -1.0), False)
    
        self.assertEqual(CurrentBalance.check_account_balance(conn, 'EmanueleP'), 0.2)

    def test_withdrawal_when_insufficient(self):

        with mock.patch('Withdrawal.Login.check_user_password') as loginMock:
            loginMock.return_value = None
            with mock.patch('Withdrawal.CurrentBalance.check_account_balance') as balanceMock:
                balanceMock.return_value = None          

                self.assertEqual(Withdrawal.withdrawal_on_account_balance(conn, 'EmanueleP', 'abcd1234', 1.0), False)
    
        self.assertEqual(CurrentBalance.check_account_balance(conn, 'EmanueleP'), 0.2)


if __name__ == '__main__':

    unittest.main()

