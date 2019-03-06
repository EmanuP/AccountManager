import sqlite3
import Login
import CurrentBalance

def deposit_on_account_balance(conn, usr, deposit):
    """
    Check for the existence of a specified user in the database
    :param conn: the Connection object
    :param id_pub: user
    :param deposit: amount to deposit
    :return: True if transaction preceeded
    """

    id_pub = Login.check_user_existence(conn, usr)
    balance = CurrentBalance.check_account_balance(conn, usr)

    if id_pub is not None and deposit > 0:

        new_balance = round(balance + deposit, 2)

        cur = conn.cursor()

        cur.execute(''' UPDATE accounts
                        SET balance = ?
                        WHERE id_pub = ?''', (new_balance, id_pub,))
        return True
    else:
        return False

