
from flask import Flask
from goods import get_goods
from users import register
from orders import app_orders
from cart import app_cart
"""
循环导入，解决方法:
1、推迟一方的导入，让另一方先完成
"""

app = Flask(__name__)

#采用装饰器方式
app.route("/get_goods")(get_goods)
app.route("/register")(register)

#注册蓝图
app.register_blueprint(app_orders,url_prefix="/orders")
app.register_blueprint(app_cart,url_prefix="/cart")

@app.route("/")
def index():
    return "index page"


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)