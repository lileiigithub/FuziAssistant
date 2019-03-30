# -*- coding: utf-8 -*-
from fuziLog import FzLog
import sqlite3
import os
from datetime import datetime

class Database(object):
    database_file = 'fuzi.db'
    def __init__(self):
        if os.path.exists(Database.database_file)==False:
            self.init_database()
        # self.c = self.conn.cursor()

    def init_database(self):
        conn = sqlite3.connect(Database.database_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE FAMILY_INFO
               (ID INT PRIMARY KEY         NOT NULL,
                DATETIME     TEXT         NOT NULL,
               FAMILY_INDEX      INT2         NOT NULL,
               YOUNG_NAME     TEXT         NOT NULL,
               YOUNG_GENDER   BOOLEAN      NOT NULL,
               RELATION       CHARACTER(10)  NOT NULL,
               OLD_NAME       TEXT         NOT NULL,
               OLD_GENDER     BOOLEAN      NOT NULL);''')
        conn.commit()
        conn.close()
        FzLog.info("Create database fuzi.db successfully")

    @staticmethod
    def insert_a_family_info(_id,_family_index,_young_name,_young_gender,
                    _relation,_old_name,_old_gender):
        conn = sqlite3.connect(Database.database_file)
        c = conn.cursor()
        data_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        COMMAND = '''INSERT INTO FAMILY_INFO(ID,DATETIME,FAMILY_INDEX,YOUNG_NAME,YOUNG_GENDER,RELATION,OLD_NAME,OLD_GENDER)
         VALUES('''+ Database._str(_id)+Database._str(data_time)+Database._str(_family_index)+Database._str(_young_name)\
                  + Database._str(_young_gender)+ Database._str(_relation)+ Database._str(_old_name)+ Database._str(_old_gender,"")+");"
        try:
            c.execute(COMMAND)
            conn.commit()
        except Exception as e: # 发生错误
            FzLog.error("Insert COMMAND:%s ERROR: %s", COMMAND, e)
        else:
            FzLog.info("Success Insert an information: %s", COMMAND)
        conn.close()

    @staticmethod
    def _str(_value, _comma = ","):
        return "'"+str(_value)+"'"+_comma

    @staticmethod
    def last_id():
        conn = sqlite3.connect(Database.database_file)
        c = conn.cursor()
        COMMAND = '''SELECT ID FROM FAMILY_INFO'''
        c.execute(COMMAND)
        # conn.commit()
        ids = []
        for row in c:
            ids.append(row[0])
        conn.close()
        return ids[-1]


if __name__ == '__main__':
    db = Database()
    # db.insert_a_family_info(2,1,"赵",1,"爷爷","钱",1)
    db.last_id()