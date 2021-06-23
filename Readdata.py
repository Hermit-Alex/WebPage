# -*- coding = utf-8 -*-
# @Time : 2021/3/27 15:30
# @Author : Hermit 
# @Fill : Readdata.py
# @software : PyCharm
import numpy as np
import os
import subprocess
import DBOperation
def readFakeData():
    x = np.random.random()
    y = np.random.random()
    z = np.random.random()
    return {
        "x":x,
        "y":y,
        "z":z
    }
def readTrackData():
    DBPath = "Machine.db"
    cor = DBOperation.readData(DBPath)
    return {
        "x":cor[0],
        "y":cor[1],
        "z":cor[2]
    }


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


if __name__ == "__main__":
    DBPath = "Machine.db"
    # mcData = ['-641.0068', '-143.3987', '0.1379', '0', '0', '0', '']
    # DBOperation.saveData(DBPath,mcData[5],mcData[4],str(0),mcData[0],mcData[1],mcData[2],mcData[3])
    testReadData(DBPath)
