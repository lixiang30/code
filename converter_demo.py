from flask import Flask,url_for,redirect
from werkzeug.routing import BaseConverter

#创建flask对象
#          模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route("/goods/<int:goods_id>")
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
    url = url_for("send_sms",mobile_num=18875037237)
    return redirect(url)


if __name__ == '__main__':
    #通过url_map()可以查看整个flask中的路由信息
    print(app.url_map)
    #启动flask程序
    app.run(debug=True)
