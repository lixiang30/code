from flask import Flask,session,current_app,request

app = Flask(__name__)

@app.route("/index")
def index():
    print("index page")
    # a = 1/0
    return "index page"

@app.route("/hello")
def hello():
    print("hello被执行")
    return "hello page"

@app.before_first_request
def handle_before_first_request():
    """第一次请求之前先被执行"""
    print("handle_before_first_request被执行")

@app.before_request
def handle_before_request():
    """每次请求之前都被执行"""
    print("handle_before_request")

@app.after_request
def handle_after_request(response):
    """每次请求之后(视图函数处理)被执行,前提是视图函数没有出现异常"""
    print("handle_after_request")
    return response

@app.teardown_request
def handle_teardown_request(response):
    """在每次请求之后(视图函数处理)被执行，无论视图函数是否出现异常．都被执行
        在debug=True模式下不起作用,只有在生产模式下才起作用
    """
    print("handle_teardown_request")
    return response


if __name__ == '__main__':
    app.run(debug=True)