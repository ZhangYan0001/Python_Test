name = ["Jack", "Jon", "Nick"]


def print_slice():
  print("---------------------------")


print(name)

print(name[0].title())

# python 的语法返回最后一个元素
print(name[-1])

all_name = ""
for i in range(0, 3):
  all_name += name[i] + " "

print(all_name)

name.append("Jan")
print(name)

name.insert(1, "Ted")
print(name)


def append_to_string(string: str, chars: str):
  return str(string) + str(chars)


name[0] = append_to_string(name[0], "the first")
print(name[0])

# 删除
del name[3]

print(name)

# 尾删
name.pop()
print(name)

# 根据值删除
name.remove("Ted")
print(name)

name.insert(0, "Peek")
name.insert(1, "Alice")

# 只显示排序后的列表，不改变原始列表中元素的位置
print(sorted(name))

# name.sort()
print(name)

# 翻转
name.reverse()
print(name)

# 长度

print(len(name))
print_slice()


def get_size(list_):
  index = 0
  while True:
    if list_[index] != list_[-1]:
      index += 1
    else:
      break
  return index + 1


print(get_size(name))

print_slice()
for n in name:
  print(n)

print_slice()

numbers = list(range(1, 5))
print(numbers)

even_number = list(range(1, 11, 2))
print_slice()
print(even_number)

print_slice()
squares = []

for i in range(1, 11):
  square = i ** 2
  squares.append(square)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

even_squares = [value ** 2 for value in range(1, 11, 2)]
print(even_squares)
print_slice()

players = ["Mark", "Oil", "Alk", "Elg", "Test"]

# 切片
print(players[0:2])
print(players[3:4])
print(players[0:])
print(players[-3:])
print_slice()

for player in players[:3]:
  print(player.lower())

food = ["rice", "cake", "pizza"]
new_food = food[:]

food.append("coffee")
new_food.append("tea")

print(food)
print(new_food)
print_slice()
