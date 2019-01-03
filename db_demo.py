
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

class Config():
    """配置参数"""
    #sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:huang921118@127.0.0.1:3306/db_python04"
    #设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)
#创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

#创建数据库模型类
class Role(db.Model):
    """用户角色/身份表"""
    __tablename__ = "tbl_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    users = db.relationship("User",backref="role")

    def __repr__(self):
        """定义之后可以让显示对象的时候更直观"""
        return "Role object:name=%s" % self.name

class User(db.Model):
    """用户表"""
    __tablename__ = "tbl_users" #指明数据库表名

    #手动指明主键
    id = db.Column(db.Integer,primary_key=True)#整型主键，会默认设置为自增主键

    name =  db.Column(db.String(64),unique=True)
    email = db.Column(db.String(128),unique=True)
    password = db.Column(db.String(128))

    role_id = db.Column(db.Integer,db.ForeignKey("tbl_roles.id"))

    def __repr__(self):
        return "User object:name=%s"%self.name


if __name__ == '__main__':
    #清除数据库中的所有数据,只有第一次才能用
    db.drop_all()
    #创建所有数据表
    db.create_all()
    role1 = Role(name="admin")
    #session记录对象任务
    db.session.add(role1)
    #提交任务到数据库中
    db.session.commit()

    role2 = Role(name="stuff")
    db.session.add(role2)
    db.session.commit()

    us1 = User(name='wang',email='wang@163.com',password='123',role_id=role1.id)
    us2 = User(name='zhang',email='zhang@189.com',password='456', role_id=role2.id)
    us3 = User(name='chen',email='chen@126.com', password='789', role_id=role2.id)
    us4 = User(name='zhou',email='zhou@163.com', password='432', role_id=role1.id)
    #一次提交多条数据
    db.session.add_all([us1,us2,us3,us4])
    db.session.commit()