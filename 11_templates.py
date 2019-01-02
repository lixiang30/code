from flask import Flask,render_template

app = Flask(__name__)

@app.route("/index")
def index():
    data = {
        "name":"python",
        "age":27,
        "my_dict":{"city":"成都"},
        "my_list":[1,2,3,4,5],
        "my_int":0,
    }
    return render_template("index.html",**data)

#1、自定义过滤器
def list_step2(li):
    """自定义过滤器"""
    return li[::2]

@app.template_filter("li3")
def list_step3(li):
    """自定义过滤器"""
    return li[::3]

#2、注册过滤器
app.add_template_filter(list_step2,"li2")


if __name__ == '__main__':
    app.run(debug=True)