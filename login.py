
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/login",methods=["POST"])
def login():
    #接收参数
    user_name = request.form.get("user_name")
    password = request.form.get("password")
    a = 1/0
    #参数校验
    if not all([user_name,password]):
        resp = {
            "code":1,
            "message":"invalid params"
        }
        return jsonify(resp)
    if user_name == "admin" and password == "python":
        resp = {
            "code":0,
            "message":"login success"
        }
        return jsonify(resp)
    else:
        resp = {
            "code":2,
            "message":"wrong user name or password"
        }
        return jsonify(resp)
    #返回数据


if __name__ == '__main__':
    app.run(debug=True)

