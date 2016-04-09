import sqlite3


class DataBaseManager(object):

    def __init__(self, name):
        self.con = sqlite3.connect(name, )
        self.cur = self.con.cursor()

    def create_table(self, table_name, fields):
        query = "CREATE TABLE IF NOT EXISTS " + table_name + "("
        for field in fields:
            query += field + ','
        query = query[:-1]
        query += ")"
        self.cur.execute(query)

    def exec_query(self, query):
        self.cur.execute(query)
        return self.cur.fetchone()

    def insert(self, table_name, fields):
        query = "INSERT INTO " + table_name + " VALUES("
        for i in xrange(len(fields[0])):
            query += '?,'
        query = query[:-1]
        query += ")"
        self.cur.executemany(query, fields)

    def last_id(self, table_name):
        rows = self.get_rows(table_name)
        return int(rows[-1][0])
        # return self.cur.lastrowid

    def get_rows(self, table_name):
        self.cur.execute("SELECT * FROM " + table_name)
        rows = self.cur.fetchall()
        return rows

    def print_table(self, table_name):
        rows = self.get_rows(table_name)
        for row in rows:
            print row

    def get_dict_from_table(self,table_name):
        # Turn a list with sqlite3.Row objects into a dictionary
        dictionary = {}  # the dictionary to be filled with the row data and to be returned

        for i, row in enumerate(self.get_rows(table_name)): # iterate throw the sqlite3.Row objects
            fields = [] # for each Row use a separate list
            for col in range(0, len(row)): # copy over the row date (ie. column data) to a list
                fields.append(row[col])
            dictionary[fields[1]] = (fields[2], fields[3]) # add the list to the dictionary
        return dictionary

    def set_dict_to_table(self,table_name,dict):
        keys = ','.join(dict.keys())
        i = 1
        for word in dict.keys():
            value = dict[word]
            self.cur.execute("INSERT INTO "+ table_name +" VALUES (" + str(i) + ",'" + word + "'," + str(value[0]) + "," + str(value[1]) + ")" )
            i += 1
        self.con.commit()

    def close_connection(self):
        self.con.commit()
        self.con.close()
