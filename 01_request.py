from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/index",methods=["GET","POST"])
def index():
    #request中包含了前端发过来的所有数据
    #通过request.form可以直接提取请求体中表单格式的数据，是一个类字典对象
    #通过get方法只能拿到多个同名参数的第一个
    #
    name = request.form.get("name","zhangsan")
    age = request.form.get("age",18)
    return "hello name=%s,age=%s" % (name,age)

if __name__ == "__main__":
    app.run(debug=True)