# -*- coding = utf-8 -*-
# @Time : 2021/4/20 15:10
# @Author : Hermit 
# @Fill : DBOperation.py
# @software : PyCharm
import  sqlite3
import DateTime


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


def saveData(dbpath,spindle_load, spindle_speed, moter_vibration,cutterpos_x,cutterpos_y,cutterpos_z,feedrate):

    data = [spindle_load, spindle_speed, moter_vibration,cutterpos_x,cutterpos_y,cutterpos_z,feedrate]
    conn = sqlite3.connect(dbpath)# 有则联结 没有则创建该数据库
    print('成功打开/建立数据库！')
    c = conn.cursor() # 获取游标 游标是查询数据库后查询到的结果
    sql = '''
    insert into MachineData(spindle_load, spindle_speed, moter_vibration,cutterpos_x,cutterpos_y,cutterpos_z,feedrate)
    values (%s);
    ''' % ",".join(data)
    print(sql)
    #SQL语句
    c.execute(sql)#执行SQL语句
    conn.commit()#提交事务 结束该事务
    conn.close()#关闭数据库连接
    print('成功插入数据！')

def readData(dbpath):
    cor = []# 坐标列表
    sql ='''
    select * from MachineData
    order by timestamp desc limit 1
    '''
    conn = sqlite3.connect(dbpath)  # 连接 有数据库就连接 没有就创建
    cursor = conn.cursor()  # 获取游标
    cursor.execute(sql)  # 执行SQL语句
    for row in cursor:
        cor.append(row[4])
        cor.append(row[5])
        cor.append(row[6])
    conn.commit()  # 结束数据库事务
    conn.close()  # 关闭连接
    return cor