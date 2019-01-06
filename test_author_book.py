
import unittest
from author_book import Author,db,app

class DatabaseTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:huang921118@127.0.0.1:3306/flask_test"
        db.create_all()

    def test_add_author(self):
        """测试添加作者的数据库操作"""
        author = Author(name="huang",email="123@qq.com",mobile="15283222652")
        db.session.add(author)
        db.session.commit()

        result_author = Author.query.filter_by(name="huang").first()
        self.assertIsNotNone(result_author)
        import time
        time.sleep(30)

    def tearDown(self):
        """在所有测试执行后执行,通常用来进行清理操作"""
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()