from flask import Flask,render_template,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)

app.config["SECRET_KEY"] = "HVHDKDVTG"


#定义表单的模型类
class RegisterForm(FlaskForm):
    """自定义的注册表单模型类"""
    #label说明标签,validators验证器,DataRequired保证数据必须填写，并且不能为空,括号里填写错误提示信息
    user_name = StringField(label="用户名",validators=[DataRequired("用户名不能为空")])
    password = PasswordField(label="密码",validators=[DataRequired("密码不能为空")])
    password2 = PasswordField(label="确认密码",validators=[DataRequired("密码不能为空")
        ,EqualTo("password","两次密码不一致")])

    submit = SubmitField(label="提交")

@app.route("/register",methods=["GET","POST"])
def register():
    #创建一个对象,如果是post请求,前端发送了数据,flask会把数据在构造form对象的时候,存放到对象中
    form = RegisterForm()
    #判断form中的数据是否合理
    #如果form中的数据都满足验证器的验证，则返回真，否则返回假
    if form.validate_on_submit():
        #表示验证合格
        #提取数据
        uname = form.user_name.data
        pwd = form.password.data
        pwd2 = form.password2.data
        print(uname,pwd,pwd2)
        session["username"] = uname
        return redirect(url_for("index"))

    return render_template("register.html",form=form)

@app.route("/index")
def index():
    user_name = session.get("username","")
    return "hello %s" % user_name



if __name__ == '__main__':
    app.run(debug=True)