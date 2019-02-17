---
title: Python Web框架之Flask入门笔记
date: 2018-01-12 12:35:15
author: Huang Bo
top: true
img: images/requests_urllib.png
mathjax: false
categories: 
- WEB框架   
- 后端开发   
tags:
- Flask
- 后端
---  

##　１ 初识Flask   
&nbsp;&nbsp;&nbsp;&nbsp;Flask诞生于2010年,是Armin ronacher用Python语言基于`Werkzeug`工具编写的轻量级WEB开发框架,它主要面向需求简单的小应用。   
&nbsp;&nbsp;&nbsp;&nbsp;Flask本身相当于一个内核，其他几乎所有的功能都要用到扩展(比如,邮件扩展Flask-Mail,用户认证Flask-Login)。也可以用Flask-extension加入`ORM`,窗体验证工具,文件上传，身份验证等。Flask没有默认使用的数据库,我们可以选择Mysql,Oracle等关系型数据库,也可以选择一些NoSQL数据库。其中,`WSGI`工具箱采用`Werkzeug`(路由模块),模板引擎则使用Jinja2。   
&nbsp;&nbsp;&nbsp;&nbsp;实际上,Flask框架的核心就是`Werkzug`和`Jinja2`。   
### 1.1 Flask和Ｄjango的对比   
&nbsp;&nbsp;&nbsp;&nbsp;总的来说,,Flask短小精悍,Django系统全面。   
&nbsp;&nbsp;&nbsp;&nbsp;主要是因为Django中集成了非常多的功能,比如:   
&nbsp;&nbsp;&nbsp;&nbsp;django-admin快速创建工程目录   
&nbsp;&nbsp;&nbsp;&nbsp;manage.py管理项目工程   
&nbsp;&nbsp;&nbsp;&nbsp;ORM模型(数据库抽象层)    
&nbsp;&nbsp;&nbsp;&nbsp;admin后台管理站点     
&nbsp;&nbsp;&nbsp;&nbsp;缓存机制   
&nbsp;&nbsp;&nbsp;&nbsp;文件存储系统   
&nbsp;&nbsp;&nbsp;&nbsp;用户认证系统    
&nbsp;&nbsp;&nbsp;&nbsp;……   
&nbsp;&nbsp;&nbsp;&nbsp;而Flask则什么都没有,需要安装额外的扩展来实现。可以说,Django就好像一个安装了许许多多扩展的Flask。   
### 1.2一些常见的扩展包以及Flask参考文档   
&nbsp;&nbsp;&nbsp;&nbsp;**常见扩展:**   
&nbsp;&nbsp;&nbsp;&nbsp;操作数据库:Flask-SQLalchemy   
&nbsp;&nbsp;&nbsp;&nbsp;管理迁移数据库:Flask-migrate   
&nbsp;&nbsp;&nbsp;&nbsp;邮件:Flask-Mail   
&nbsp;&nbsp;&nbsp;&nbsp;表单:Flask-WTF    
&nbsp;&nbsp;&nbsp;&nbsp;插入脚本:Flask-script   
&nbsp;&nbsp;&nbsp;&nbsp;认证用户状态:Flask-Login   
&nbsp;&nbsp;&nbsp;&nbsp;开发REST API工具:Flask-RESTful   
&nbsp;&nbsp;&nbsp;&nbsp;集成前端Twitter Bootsrap:Flask-Bootstrap   
&nbsp;&nbsp;&nbsp;&nbsp;本地化时间和日期:Flask-Moment   
&nbsp;&nbsp;&nbsp;&nbsp;**参考文档：**   
&nbsp;&nbsp;&nbsp;&nbsp;[中文文档](http://docs.jinkan.org/docs/flask/)   
&nbsp;&nbsp;&nbsp;&nbsp;[英文文档](http://flask.pocoo.org/docs/0.11/) 

---  
## 2 Flask基础入门    
### 2.1 Hello flask 
```python
from flask import Flask

#创建flask对象
#__name__表示当前模块名
#          模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(
            __name__,
            static_url_path="/python",
            static_folder="static",
            template_folder="templates"
)

# 1、 使用配置文件
# app.config.from_pyfile('config.cfg')
#2、使用对象配置
class Config(object):
    DEBUG = True
    SCHOOL = "ChongQing University"
    
app.config.from_object(Config)
#3 直接操作config的字典对象
# app.config["DEBUG"] = True

@app.route("/") #路由使用装饰器的方式
def index():
    """定义视图函数"""
    return "hello flask!"

if __name__ == '__main__':
    #启动flask程序
    app.run(host='0.0.0.0',port=5000,debug=True)
```   
### 2.2 Flask应用对象初始化参数说明  
&nbsp;&nbsp;&nbsp;&nbsp;**\_\_name__:** `__name__`指的是当前模块名,如果以该模块作为启动文件,则`__name__`表示`__main__`,如果不作为启动文件则表示该模块的模块名。   
&nbsp;&nbsp;&nbsp;&nbsp;**static_url_path:** 静态资源的访问路径,默认是`static`
&nbsp;&nbsp;&nbsp;&nbsp;**static_folder:** 静态文件的目录,默认是`static`  
&nbsp;&nbsp;&nbsp;&nbsp;**template_folder:** 模板文件目录,默认是`templates`   

&nbsp;&nbsp;&nbsp;&nbsp;**Flask的配置参数设置:**   
&nbsp;&nbsp;&nbsp;&nbsp;a.使用配置文件,新建config.cfg配置文件,然后去需要引入配置文件的模块里执行`app.config.from_pyfile("config.cfg")`   
&nbsp;&nbsp;&nbsp;&nbsp;b.使用类的方式,定义Config类,然后执行`app.config.from_object(Config)`   
&nbsp;&nbsp;&nbsp;&nbsp;c.直接采用读取字典的方式,`app.config["键名xx""]=xx`   

&nbsp;&nbsp;&nbsp;&nbsp;**获取配置参数的方式:**   
&nbsp;&nbsp;&nbsp;&nbsp;对于一些全局的配置参数,比如，上面示例代码的`SCHOOL`，如果是在本文件获取可以采用字典的形式,除此之外,如果是采用了蓝图等路由划分的，可以使用`current_app`来获取,示例：`current_app.config.get("SCHOOL")`  

### 2.3 Flask的路由简单说明   
&nbsp;&nbsp;&nbsp;&nbsp;**ur_map:**可以查看整个flask中的路由信息
&nbsp;&nbsp;&nbsp;&nbsp;**methods:**限定访问方式   
&nbsp;&nbsp;&nbsp;&nbsp;**url_for:**使用`url_for`的函数,通过视图函数的名字找到视图函数对应的url路径   
```python
from flask import Flask,url_for,redirect

#创建flask对象
#          模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route("/")
def index():
    """定义视图函数"""
    return "hello flask!"

@app.route('/post_only',methods=["POST","GET"])#　methods可以限定访问方式
def post_only():
    return "post_only"

@app.route("/hello") #路由相同访问方式相同，会访问前面的
def hello1():
    return "hello1"
@app.route("/hello")
def hello2():
    return "hello2"

@app.route("/test1")#一个视图函数,多个路由
@app.route("/test2")
def test():
    return "test"

@app.route('/login')
def login():
    url = url_for("test") #url_for可以通过函数名，去找函数对应的路径
    return redirect(url)

if __name__ == '__main__':
    #通过url_map()可以查看整个flask中的路由信息
    print(app.url_map)
    #启动flask程序
    app.run(debug=True)
```   
### 2.3 自定义转换器   
```python
from flask import Flask,url_for,redirect
from werkzeug.routing import BaseConverter

#创建flask对象
#          模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route("/goods/<int:goods_id>") #不加转换器类型,默认是普通字符串规则(除了/的规则)
def goods_detail(goods_id):
    return "goods detail page,%s"%(goods_id)

#定义自己的转换器(手机的)
class MobileConverter(BaseConverter):
    def __init__(self,url_map):
        super(MobileConverter, self).__init__(url_map)
        self.regex = r'1[34578]\d{9}'

# 1 自定义转换器
class RegexConverter(BaseConverter):
    """转换器"""
    def __init__(self,url_map,regex):
        #调用父类的初始化方法
        super().__init__(url_map)
        #将正则表达式的参数保存到对象属性中，flask会去使用这个属性来进行路由的正则匹配
        self.regex = regex

    def to_python(self, value):
        #value是路径表达式进行正则匹配的时候提取的参数
        return value
    def to_url(self, value):
        #使用url_for方法时自动被调用
        return value

# 2 将自定义的转换器添加到flask中
app.url_map.converters['re'] = RegexConverter
app.url_map.converters['mobile'] = MobileConverter

@app.route("/send/<re(r'1[34578]\d{9}'):mobile_num>")
# @app.route("/send/<mobile:mobile_num>")
def send_sms(mobile_num):
    return "send sms to %s"%(mobile_num)

@app.route("/index")
def index():
    url = url_for("send_sms",mobile_num="18875037238")
    return redirect(url)


if __name__ == '__main__':
    #通过url_map()可以查看整个flask中的路由信息
    print(app.url_map)
    #启动flask程序
    app.run(debug=True)

```   

### 2.4 获取请求参数   
&nbsp;&nbsp;&nbsp;&nbsp;`request`是Flask中表示请求当前请求的request对象,request对象中保存了一次HTTP请求的一切信息。Flask中引入reuest的方法`from flask import request`,request常用属性如下表所示:   

| 属性 | 说明 | 类型 |
| ------ | ------ | ------ |
| data | 记录请求的数据，并转换为字符串 | * |
| form | 记录请求中的表单数据 | MultiDict |
| args | 记录请求中的查询参数 | MultiDict |
| cookies| 记录请求中的cookies信息 | Dict |
| headers | 记录请求中的报文头 | EnvironHeaders | 
| method | 记录请求使用的HTTP方法 | GET/POST |
| url | 记录请求的URL地址 | string |
| files | 记录请求上传的文件 | * |    

&nbsp;&nbsp;&nbsp;&nbsp;**测试代码:(可以利用Postman快速测试)**   
```python
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
```   

&nbsp;&nbsp;&nbsp;&nbsp;**上传文件:**   
&nbsp;&nbsp;&nbsp;&nbsp;已上传的文件在内存或是文件系统中一个临时的位置。我们可以通过请求对象的files属性访问它们。每个文件都会存储在这个字典里。我们可以利用save()方法,把文件保存到指定位置。   
```python
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/upload",methods=["POST"])
def upload():
   """接受前端传过来的文件"""
   file_obj = request.files.get("pic") #文件名叫pic
   if  file_obj is None:
       # 表示没有发送文件
        return "未上传文件"

   # #将文件保存到本地
   # #1 创建一个文件
   # f = open("./demo.jpg","wb")
   # #2 向文件写内容
   # data = file_obj.read()
   # f.write(data)
   # #3 关闭文件
   # f.close()
   #直接使用上传的文件对象
   file_obj.save("./demo1.jpg")
   return "上传成功"

if __name__ == "__main__":
    app.run(debug=True)
```      

### 2.5 with的用法
 

