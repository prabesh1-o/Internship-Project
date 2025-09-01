
# def decor1(fun):
#     def inner():
#         b = fun()
#         mul = b*5
#         return mul
#     return inner


# def num():
#     return 10
# n1 = decor1(num)
# print(n1())

# decorator


# def decor1(fun):
#     def inner():
#         print("IF:Before enhancing the function")
#         fun()
#         print("after enhancig the function")
#     return inner

# @decor1
# def num():
#     print("we will use this function")
#     print(" And we will enhance  this function")
# # result= decor1(num)
# # print(result())
# num()


def decorator1(func):
    def inner():
        b = func()
        mul = b*5
        return mul
    return inner

@decorator1
def num():
    return 5
# res = decorator1(num)
# print(res())
num()