#functions 
# #EX1
# def loop():
#     for i in range(10):
#         print(i)
#         if i == 3:
#             return
# loop();

# #EX2
# #important example
# def twice (x, y):
#     return y(y(x))

# def mul (x):
#     return x**3

# obj = twice(2, mul)
# print(obj)

# #EX3
# def fun1(x):
#     def fun2(y):
#         return y+2
#     return 3*fun2(x)
# fun1(2)
# print(fun1(2))

# #EX4
# x = 1
# def add_one (x):
#     x = x + 1
#     # add one to the local x
#     return x


# # call the function
# y = add_one (2)
# print(x)
# print(y)

# #EX5
# def f1():
#     global x
#     x = x + 1
#     return x

# def f2():
#     return  x+2

# def f3():
#     x = 5
#     return x+1 


# x = 0
# print(f1()) 
# print(f2()) 
# print(f3()) 
