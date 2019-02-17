
from flask import Flask,request,abort,Response,make_response

app = Flask(__name__)

@app.route("/index")
def index():
    # 1.使用元组,返回自定义的响应信息
    #       响应体　　　　状态码(可以加解释性文字)　　　　响应头(可以字典或者元组的形式)
    # return "index page",400,[("Itcast","python"),("City","Shenzhen")]
    # return "index page2", "666 666 status", {"Itcast1":"python1","City1":"sz1"}

    # 2. 使用make_response来构建响应信息
    resp = make_response("index page 3")
    resp.status = "999 status" # 设置状态码
    resp.headers["city"] = "chengdu" # 设置响应头
    return resp

if __name__ == "__main__":
    app.run(debug=True)