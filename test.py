# -*- coding = utf-8 -*-
# @Time : 2021/4/20 15:56
# @Author : Hermit 
# @Fill : test.py
# @software : PyCharm
import os
import subprocess
import DBOperation
import sqlite3
# -641.0068
# -143.3987
# 0.1379
# feed rate：0mm/min
# spindle speed: 0degree
# spindle load: 0

def testReadData(DBPath):
    order = r".\readdata\Test.exe"
    pi = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
    index = 0
    mcData = []# x y z fr sps spl v设为0
    try:
        for i in iter(pi.stdout.readline, 'b'):
            item = i.decode('gbk')  # 编码问题
            item = item[:-2] # 去掉\r\n
            mcData.append(item)
            if item =='':
                print(mcData)
                DBOperation.saveData(DBPath, mcData[5], mcData[4], str(0), mcData[0], mcData[1], mcData[2], mcData[3])
                mcData = []
    except ValueError as e:
        print(str(e))

def readData(dbpath):
    cor = []# 坐标列表
    cors = []
    sql ='''
    select cutterpos_x,cutterpos_y,cutterpos_z from MachineData
    order by timestamp desc limit 800
    '''
    conn = sqlite3.connect(dbpath)  # 连接 有数据库就连接 没有就创建
    cursor = conn.cursor()  # 获取游标
    cursor.execute(sql)  # 执行SQL语句
    for row in cursor:
        cor.append(row[0])
        cor.append(row[1])
        cor.append(row[2])
        if len(cor)==3:
            cors.append(cor)
            cor =[]
    conn.commit()  # 结束数据库事务
    conn.close()  # 关闭连接
    return cors


DBPath = "Machine.db"
print(readData(DBPath))