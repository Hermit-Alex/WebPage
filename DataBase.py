# -*- coding = utf-8 -*-
# @Time : 2021/4/16 10:56
# @Author : Hermit 
# @Fill : DataBase.py
# @software : PyCharm


import  sqlite3 #引入SQLite3 数据库包
def init_db(dbpath):
    sql = '''
    create table if not exists MachineData (
    TimeStamp NOT NULL DEFAULT (datetime('now','localtime')),
    spindle_load numeric,
    spindle_speed numeric,
    moter_vibration numeric,
    cutterpos_x numeric,
    cutterpos_y numeric,
    cutterpos_z numeric,
    feedrate numeric
    )
    '''#SQL语句
    conn = sqlite3.connect(dbpath)#连接 有数据库就连接 没有就创建
    cursor = conn.cursor()#获取游标

    cursor.execute(sql)#执行SQL语句
    conn.commit()#结束数据库事务
    conn.close()#关闭连接

if __name__=="__main__":
    path = "Machine.db"
