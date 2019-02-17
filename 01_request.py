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
    city = request.args.get("city")
    name2 = request.form.getlist("name")
    print(request.data)
    print(request.form)
    return "hello name=%s,age=%s,city=%s,name2=%s" % (name,age,city,name2)

if __name__ == "__main__":
    app.run(debug=True)