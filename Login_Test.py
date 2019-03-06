import sqlite3

from Dummy_DB import create_dummy, delete_dummy
import unittest

import Login

conn = create_dummy("./test.db")

class TestLoginMethods(unittest.TestCase):

    def test_existence_when_existing(self):
        self.assertEqual(Login.check_user_existence(conn, 'EmanueleP'), 512)

    def test_user_existence_when_non_existing(self):
        self.assertEqual(Login.check_user_existence(conn, 'PincoP'), None)

    def test_user_password_when_correct(self):
        self.assertEqual(Login.check_user_password(conn, 'EmanueleP', 'abcd1234'), 1)

    def test_user_password_when_usr_incorrect(self):
        self.assertEqual(Login.check_user_password(conn, 'PincoP', 'abcd1234'), None)

    def test_user_password_when_psw_incorrect(self):
        self.assertEqual(Login.check_user_password(conn, 'EmanueleP', '1234abcd'), None)

    def tearDownClass():
        conn.close()
        delete_dummy("./test.db")



if __name__ == '__main__':

    unittest.main()
    
