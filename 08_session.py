from flask import Flask,session

app = Flask(__name__)

#flask的session需要用到的秘钥字符串
app.config["SECRET_KEY"] = "fdsahjlk"

#flask默认把session保存到了cookie中

@app.route("/login")
def login():
    # 设置session数据
    session["name"] = "python"
    session["mobile"] = "18875037238"
    return "login sucess"

@app.route("/index")
def index():
    # 获取session数据
    name = session.get("name")
    return "hello %s"%name



if __name__ == '__main__':
    app.run(debug=True)