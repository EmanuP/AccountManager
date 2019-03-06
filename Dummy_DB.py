import sqlite3, os

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def add_user(conn, usr):
    """
    Create a new user into the accounts table
    :param conn: Connection object
    :param usr: User parameters
    :return: user id
    """
    sql = ''' INSERT INTO accounts(id_pub,user,password,balance)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, usr)
    return cur.lastrowid

def create_dummy(database):
    """
    Create a new user into the accounts table
    :param database: database name
    :return: Connection Object
    """
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS accounts (
                                        id integer PRIMARY KEY,
                                        id_pub integer,
                                        user text NOT NULL,
                                        password text NOT NULL,
                                        balance real
                                    ); """

    user_1 = (512, 'EmanueleP', 'abcd1234', 1.2)
    user_2 = (127, 'AntoC', 'abcd1234', 0.0)

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create users table
        create_table(conn, sql_create_users_table)
        # add user_1
        user1_id = add_user(conn, user_1)
        # add user_2
        user2_id = add_user(conn, user_2)

    return conn

def delete_dummy(database):
    """
    Create a new user into the accounts table
    :param database: database name
    :return: 
    """
    print(os.path.exists(database))
    if os.path.exists(database):
        os.remove(database)