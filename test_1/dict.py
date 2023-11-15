def print_slice():
  print("------------------------------")


print_slice()
alien_0 = {"color": "green", "points": 5}

print(alien_0)
alien_0["color"] = "yellow"

print(alien_0)

# del alien_0["points"]
# print(alien_0)

print_slice()
for k, v in alien_0.items():
  print("Key:" + k)
  print("Value:", v)

print_slice()
for k in alien_0.keys():
  print("Key:" + k)

print_slice()
for k in sorted(alien_0.keys()):
  print("Key:" + k)

print_slice()
for v in set(alien_0.values()):
  print("Value:", v)

alien_1 = {"color": "green", "points": 3}
alien_2 = {"color": "yellow", "points": 6}
alien_3 = {"color": "red", "points": 8}

aliens = [
  alien_0,
  alien_1,
  alien_2,
  alien_3,
]
print(type(alien_0))
