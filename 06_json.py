from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/index")
def index():
    #json字符串
    data = {
        "name":"zhangsan",
        "age":27,
    }
    #json.dumps(字典),将python字典转换为json字符串
    #json.loads(字符串),将python中json字符串转换为python中的字典
    # json_str = json.dumps(data)
    # return json_str,200,{"Content-Type":"application/json"}

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)