i = 1
while i < 10:
  j = 1
  while j <= i:
    print("%d * %d = %d\t" % (j, i, i * j), end=(""))
    j += 1
  print("")
  i += 1

print("\n")

for i in range(1, 10):
  for j in range(1, i+1):
    print("%d * %d = %d\t" % (j, i, i*j), end=(""))
  print()

print("\n")
i = 9
while i >= 1:
  for j in range(1, i+1):
    print("%d * %d = %d\t" % (j, i, j*i), end="")
  i -= 1
  print()
