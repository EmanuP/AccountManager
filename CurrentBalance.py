import sqlite3
import Login


def check_account_balance(conn, usr):
    """
    Check for the existence of a specified user in the database
    :param conn: the Connection object
    :param usr: user
    :param psw: password
    :return: account balance
    """

    id_pub = Login.check_user_existence(conn, usr)

    if id_pub is not None:
        cur = conn.cursor()
        cur.execute("SELECT balance FROM accounts WHERE id_pub=?", (id_pub,))
        balance = cur.fetchall()[0][0]
        return balance
    else:
        return None
