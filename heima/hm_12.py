def sum_2_num(num1, num2):
    """对两个数字求和"""

    result = num1 + num2

    # 可以使用返回值，告诉调用函数一方计算的结果
    return result


sum_result = sum_2_num(10, 15)
# 可以使用变量，来接收函数执行的返回的结果

print("计算结果： %d" % sum_result)