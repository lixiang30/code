from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

#引入mysql驱动
import pymysql
pymysql.install_as_MySQLdb()

class Config(object):
    #sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:huang921118@127.0.0.1:3306/author_book_py04"
    #设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = "sdafvhxdfsfn"

app.config.from_object(Config)

db = SQLAlchemy(app)

#定义表

class Author(db.Model):
    """作者表"""
    __tablename__ = "tbl_authors"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    books = db.relationship("Book",backref="author")

class Book(db.Model):
    """书籍表"""
    __tablename__ = "tbl_books"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    author_id = db.Column(db.Integer,db.ForeignKey("tbl_authors.id"))


#创建表单模型类
class AuthorBookForm(FlaskForm):
    """作者书籍表单模型类"""
    author_name = StringField(label="作者",validators=[DataRequired("作者必填")])
    book_name = StringField(label="书籍",validators=[DataRequired("书籍必填")])
    submit =SubmitField(label="保存")

@app.route("/",methods=["GET","POST"])
def index():
    #创建表单对象
    form = AuthorBookForm()
    if form.validate_on_submit():
        #验证成功，提取数据
        author_name = form.author_name.data
        book_name = form.book_name.data
        #保存从前端获取的数据，存到数据库
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name,author=author)
        db.session.commit()
    #查询数据库
    authors_li = Author.query.all()
    return render_template("author_book.html",authors = authors_li,form=form)

if __name__ == '__main__':
    app.run(debug=True)
    # db.drop_all()
    # db.create_all()
    # au_xi = Author(name='我吃西红柿')
    # au_qian = Author(name='萧潜')
    # au_san = Author(name='唐家三少')
    # db.session.add_all([au_xi, au_qian, au_san])
    # db.session.commit()
    #
    # bk_xi = Book(name='吞噬星空', author_id=au_xi.id)
    # bk_xi2 = Book(name='寸芒', author_id=au_qian.id)
    # bk_qian = Book(name='飘渺之旅', author_id=au_qian.id)
    # bk_san
    # = Book(name='冰火魔厨', author_id=au_san.id)
    # db.session.add_all([bk_xi, bk_xi2, bk_qian, bk_san])
    # db.session.commit()