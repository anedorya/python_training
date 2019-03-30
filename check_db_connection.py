import pymysql.cursors
# from fixture.db import DbFixture
from fixture.orm import ORMfixture
from model.group import Group

db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")
# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id=191))
    for item in l:
        print(item)
    print(len((l)))
finally:
    pass # db.destroy()



# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)

# finally:
#     connection.close()
