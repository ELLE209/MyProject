import sqlite3


class DataBaseManager(object):

    # constructor
    def __init__(self, name):
        self.con = sqlite3.connect(name, )
        self.cur = self.con.cursor()

    # create a table in db
    def create_table(self, table_name, fields):
        """
        :param table_name: name of new table to create
        :param fields: structure of fields for that table
        :return: builds a suitable query and executes it
        """
        query = "CREATE TABLE IF NOT EXISTS " + table_name + "("
        for field in fields:
            query += field + ','

        # remove the last ',' and close with ')'
        query = query[:-1]
        query += ")"

        self.cur.execute(query)

    # executes a given query
    def exec_query(self, query):
        """
        :param query: query to execute
        :return: query return values
        """
        self.cur.execute(query)
        return self.cur.fetchone()

    # insert values to table in db
    def insert(self, table_name, fields):
        """
        :param table_name: the table to insert into
        :param fields: values to be inserted
        :return: builds a suitable query and executes it
        """
        query = "INSERT INTO " + table_name + " VALUES("
        for i in xrange(len(fields[0])):
            query += '?,'

        # remove the last ',' and close with ')'
        query = query[:-1]
        query += ")"

        self.cur.executemany(query, fields)

    # get last row num(ID)
    def last_id(self, table_name):
        """
        :param table_name: the table to check
        :return: id of last row in table
        """
        rows = self.get_rows(table_name)
        return int(rows[-1][0])

    # get all rows of a table
    def get_rows(self, table_name):
        """
        :param table_name: the table to get rows frm
        :return: builds a suitable query and executes it
        """
        self.cur.execute("SELECT * FROM " + table_name)
        rows = self.cur.fetchall()
        return rows

    # print all table values
    def print_table(self, table_name):
        """
        :param table_name: table to print
        :return: None
        """
        rows = self.get_rows(table_name)
        for row in rows:
            print row

    # close connection with db file
    def close_connection(self):
        self.con.commit()
        self.con.close()
