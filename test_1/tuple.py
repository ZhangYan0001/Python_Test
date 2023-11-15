dimensions = (200, 50)

print(type(dimensions))
print(dimensions)

print(dimensions[0])
print(dimensions[1])

# 禁止对元组赋值 , 无法修改
# dimensions[0] = 1

for dim in dimensions:
  print(dim)
