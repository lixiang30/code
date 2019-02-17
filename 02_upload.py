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