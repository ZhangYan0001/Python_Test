
file1 = open("./test/1.txt", 'w')
file2 = open("./test/2.txt", "w")

if file1:
  for i in range(0, 10):
    file1.write("hello world\n")
    file2.write("hi, how are you\n")
  file1.close()
  file2.close()
