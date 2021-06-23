from flask import Flask,render_template,request  # 引入flask包
import Readdata
app = Flask(__name__)  # 初始化框架


# 路由解析 用户访问的路径 匹配相应的函数
@app.route('/test',methods=["get","post"])
def hello_world():
    return   render_template("testEchartPage.html")# 执行操作

# 路由解析 用户访问的路径 匹配相应的函数
@app.route('/draw',methods=["get","post"])
def hello_world1():
    return   render_template("DrawTrack.html")# 执行操作


# 路由解析 用户访问的路径 匹配相应的函数
@app.route('/',methods=["get","post"])
def dataVisualize():
    return   render_template("index.html")# 执行操作


# 路由解析 用户访问的路径 匹配相应的函数
@app.route('/newPoint',methods=["get","post"])
def readData():
    # print("read data successful")
    return   Readdata.readTrackData()# 执行操作

if __name__ == '__main__':  # 主程序入口
    app.run()  # 运行框架
    print("正在运行")
