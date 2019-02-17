from flask import Flask,url_for,redirect
import demo

#创建flask对象
#          模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route("/")
def index():
    """定义视图函数"""
    return "hello flask!"

@app.route('/post_only',methods=["POST","GET"])#　methods可以限定访问方式
def post_only():
    return "post_only"

@app.route("/hello") #路由相同访问方式相同，会访问前面的
def hello1():
    return "hello1"
@app.route("/hello")
def hello2():
    return "hello2"

@app.route("/test1")#一个视图函数,多个路由
@app.route("/test2")
def test():
    return "test"

@app.route('/login')
def login():
    url = url_for("test") #url_for可以通过函数名，去找函数对应的路径
    return redirect(url)

if __name__ == '__main__':
    #通过url_map()可以查看整个flask中的路由信息
    print(app.url_map)
    #启动flask程序
    app.run(debug=True)
