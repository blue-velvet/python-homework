import pymysql.cursors
from model.data import Group

class DbFixture():
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        self.connection.commit()
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_footer from group_list")
            for row in cursor:
                (id, name, footer) = row
                list.append(Group(id=str(id), group_name=name, group_footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
