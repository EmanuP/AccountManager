import sqlite3
import Login
import CurrentBalance


def withdrawal_on_account_balance(conn, usr, psw, withdrawal):
    """
    Check for the existence of a specified user in the database
    :param conn: the Connection object
    :param usr: user
    :param psw: password
    :param withdrawal: amount to withdraw
    :return: True if transaction preceeded
    """

    id = Login.check_user_password(conn, usr, psw)
    balance = CurrentBalance.check_account_balance(conn, usr)

    if balance is not None and (balance-withdrawal) >= 0 and id is not None and withdrawal > 0:
        new_balance = round(balance - withdrawal, 2)
        cur = conn.cursor()
        cur.execute(''' UPDATE accounts
                        SET balance = ?
                        WHERE id = ?''', (new_balance, id,))
        return True
    else:
        return False
