
from flask import Flask,render_template,flash

app = Flask(__name__)
flag = True
app.config["SECRET_KEY"] = "qdadvvfsd"

@app.route("/")
def macro():

    if flag:
        #添加闪现信息
        flash("hello1")
        flash("hello2")
        flash("hello3")
        global flag
        flag = False

    return render_template("macro.html")

if __name__ == "__main__":
    app.run(debug=True)