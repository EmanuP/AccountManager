import sqlite3


def check_user_existence(conn, usr):
    """
    Check for the existence of a specified user in the database
    :param conn: the Connection object
    :param usr: user
    :return: the id_pub of the first match
    """
    cur = conn.cursor()
    cur.execute("SELECT id_pub FROM accounts WHERE user=?", (usr,))

    rows = cur.fetchall()

    if len(rows) > 0:
        return rows[0][0]
    else:
        return None


def check_user_password(conn, usr, psw):
    """
    Check for the existence of a specified user in the database
    Eventually check if its password is correct
    If password matches return the user ID of the first occurrence
    of the given usr,psw pair
    :param conn: the Connection object
    :param usr: user
    :param psw: password
    :return: the id of the first match
    """
    if not check_user_existence(conn, usr):
        return None

    cur = conn.cursor()
    cur.execute("SELECT id, password FROM accounts WHERE user=?", (usr,))

    rows = cur.fetchall()

    for row in rows:
        if psw == row[1]:
            return row[0]
        else:
            return None
