

import unittest
from login import app
import json

class LoginTest(unittest.TestCase):
    """构造单元测试案例"""
    def setUp(self):
        """在进行测试之前先被执行"""
        #设置flask工作在测试模式下
        #app.testing = True
        app.config["TESTING"] = True
        #创建进行web请求的客户端,使用flask提供的
        self.client = app.test_client()

    def test_empty_user_name_password(self):
        """测试用户名密码不完整的情况"""

        #利用client客户端模拟请求客户端，使用flask提供的
        ret = self.client.post("/login",data={})

        #ret是视图返回的响应对象,data属性是响应体的数据
        resp = ret.data

        #因为login视图返回的是json字符串
        resp = json.loads(resp.decode('utf8'))

        #拿到返回值之后，进行断言测试
        self.assertIn("code",resp)
        self.assertEqual(resp["code"],1)

        ######只传用户名##########
        ret = self.client.post("/login", data={"user_name":"admin"})

        # ret是视图返回的响应对象,data属性是响应体的数据
        resp = ret.data

        # 因为login视图返回的是json字符串
        resp = json.loads(resp.decode('utf8'))

        # 拿到返回值之后，进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

        ########只传密码############
        ret = self.client.post("/login", data={})

        # ret是视图返回的响应对象,data属性是响应体的数据
        resp = ret.data

        # 因为login视图返回的是json字符串
        resp = json.loads(resp.decode('utf8'))

        # 拿到返回值之后，进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

    def test_wrong_user_name_password(self):
        """测试用户名或密码错误"""
        ret = self.client.post("/login",data={"user_name":"admin","password":"test"})
        #ret是视图函数返回的对象,data是响应体的数据
        resp = ret.data
        #因为login视图函数返回的是json字符串
        resp = json.loads(resp.decode("utf8"))
        #拿到返回的值后进行断言
        self.assertIn("code",resp)
        self.assertEqual(resp["code"],2)



if __name__ == '__main__':
    unittest.main()