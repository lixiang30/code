from flask import Flask
import demo

#创建flask对象
#          模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

# 1、 使用配置文件
# app.config.from_pyfile('config.cfg')
#2、使用对象配置
class Config(object):
    DEBUG = True
app.config.from_object(Config)
#3 直接操作config的字典对象
# app.config["DEBUG"] = True

@app.route("/")
def index():
    """定义视图函数"""
    return "hello flask!"

if __name__ == '__main__':
    #启动flask程序
    app.run(host='0.0.0.0',port=5000)
