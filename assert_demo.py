

def num_div(num1,num2):
    #ａssert断言，后面是一个表达式，如果为真，则断言成功，程序继续往下执行，
    # 如果返回假，则断言失败，assert会抛出异常AsserttionError，终止程序继续往下执行
    assert isinstance(num1,int)
    assert isinstance(num2,int)
    assert num2 != 0
    print(num1/num2)

if __name__ == '__main__':
    num_div(100,50)