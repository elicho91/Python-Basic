import cx_Oracle
import datetime



class TestDAO:
    def __init__(self):
        cx_Oracle.init_oracle_client(lib_dir=r"E:\oracle\instantclient_19_16")



    def selectOne(self, data):
        conn = cx_Oracle.connect('java06', 'java06', '192.168.100.250:1521/orcl')
        cursor = conn.cursor()  # cursor 객체 얻어오기
        sql = "select * from test where id=:1"
        cursor.execute(sql, data)
        for row in cursor:
            print(row)
        cursor.close()
        conn.close()

    def selectAll(self):
        conn = cx_Oracle.connect('java06', 'java06', '192.168.100.250:1521/orcl')
        cursor = conn.cursor()  # cursor 객체 얻어오기
        sql = "select * from test"
        cursor.execute(sql)
        for row in cursor:
            print(row)
        cursor.close()
        conn.close()

    def insertUser(self, data):
        conn = cx_Oracle.connect('java06', 'java06', '192.168.100.250:1521/orcl')
        cursor = conn.cursor()  # cursor 객체 얻어오기
        sql = "insert into test values(:1, :2, :3, :4)"
        cursor.execute(sql, data)
        cursor.close()
        conn.commit()
        conn.close()

    def updateUser(self, data):
        conn = cx_Oracle.connect('java06', 'java06', '192.168.100.250:1521/orcl')
        cursor = conn.cursor()  # cursor 객체 얻어오기
        sql = "update test set pw=:1, age=:2 where id=:3"
        cursor.execute(sql, data)
        cursor.close()
        conn.commit()
        conn.close()

    def deleteUser(self, data):
        conn = cx_Oracle.connect('java06', 'java06', '192.168.100.250:1521/orcl')
        cursor = conn.cursor()  # cursor 객체 얻어오기
        sql = "delete from test where id=:1"
        cursor.execute(sql, data)
        cursor.close()
        conn.commit()
        conn.close()

dao = TestDAO()
dao.selectOne(('py01',))
print("=" * 100)
dao.selectAll()
print("=" * 100)
dao.insertUser(('python01', '1234', 30, datetime.datetime.now()))
dao.selectAll()
print("+" * 100)
dao.updateUser(('9845646541532', 123, 'pythone001'))
dao.selectOne(('python001',))
dao.deleteUser(('python002',))
dao.selectAll()