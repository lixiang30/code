

from flask import Flask,request,abort,Response

app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def login():
    # name = request.form.post()
    # pwd = request.form.post()
    name = ""
    pwd = ""
    if name != "zhangsan" or pwd != "admin":
        # 使用abort函数可以立即终止视图函数的执行
        # 并可以返回给前端特定的信息
        # 1.传递状态码信息,必须是标准的http状态码
        abort(404)
        # 2.传递响应体信息
        # resp = Response("login failed")
        # abort(resp)

    return "login success"

@app.errorhandler(404)
def handle_404_error(err):
    """自定义的处理错误方法"""
    # 这个函数的返回值是前端用户看到的最终结果
    return "出现了404错误,错误信息：%s" % err

if __name__ == '__main__':
    app.run(debug=True)