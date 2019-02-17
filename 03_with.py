
####传统方法################
#创建一个文件对象
f = open("./1.text","w")
# 向文件写内容
try:
    f.write("hello flask")
except Exception:
    pass
finally:
#关闭文件
    f.close()

#########with方法#############

with open('./2.text',"w") as f:
    f.write("hello django,hello flask,hello tornado")


"""
with称为上下文管理器，
"""

class Foo():
    def __enter__(self):
        """进入with语句时被with调用"""
        print("enter")
    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开with语句时被with调用"""
        print("exit")
        print("exc_type:%s"%exc_type)
        print("exc_val:%s"%exc_val)
        print("exc_tb:%s"%exc_tb)

with Foo() as foo:
    print("hello python")
    # a = 1 / 0
    print("111")