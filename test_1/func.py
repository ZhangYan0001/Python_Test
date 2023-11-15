from dict import print_slice as ps


def print_slice():
  print("-------------------")


def greet_user(username: str):
  """显示简单的问候语"""
  print("Hello, " + username.title() + "!")


greet_user("jan")

ps()


# 默认参数
def describe_pet(pet_name: str, animal_type="dog"):
  print("the pet name is :" + pet_name + "this is a " + animal_type)


# def get_pet_name(animal_type: str, host_name: str):
#   return "dog"


# 传递任意数量的实参
# 形参名* toppings 中的星号让python创建一个名为topping的空元组
# 并将收到的所有值的封装到这个元组中。
# 注意python将实参封装到一个元组中，即便函数只收到一个值也如此
def make_pizza(*toppings):
  print(toppings)


make_pizza("mushrooms", "green peppers", "extra cheese")


def fib(n):
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a + b
    yield a
