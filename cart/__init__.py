
from flask import Blueprint

#创建一个蓝图
app_cart = Blueprint("app_cart",__name__,template_folder="templates",static_folder="static")

#在init文件被执行的时候,把视图加载进来，让蓝图与应用程序知道使徒的存在
from .views import get_cart