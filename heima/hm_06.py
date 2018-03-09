# 定义holiday_name 字符串比那辆记录节日名称
holiday_name = input("今天是什么节日：")

# 如果是情人节应该买玫瑰看电影
if holiday_name == "情人节":
    print("买玫瑰，看电影")

# 如果是平安夜应该买苹果吃大餐
elif holiday_name == "平安夜":
    print("买苹果吃大餐")

# 如果是生日应该买蛋糕
elif holiday_name == "生日":
    print("买蛋糕")

# 其他的日志应该都是节日啊
else:
    print("每天都是节日")
