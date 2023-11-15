def print_slice():
  print("----------------------")


file_path = "./files/pi_digits.txt"

with open(file_path) as file_object:
  contents = file_object.read()
  print(contents)

print_slice()

with open(file_path, 'r') as f:
  for line in f:
    print(line.strip())

print_slice()
with open(file_path) as file_object:
  lines = file_object.readlines()

pi_string = ''
for line in lines:
  pi_string += line.rstrip()

print(pi_string)

print(len(pi_string))

write_file = "./files/write_files.txt"

with open(write_file, "w") as file_object:
  file_object.write("I Love Programing.\n")
  file_object.write("I love you.\n")

"""
追加
"""
with open(write_file, "a") as file_object:
  file_object.write("I also love finding meaning in large datasets.\n")
  file_object.write("I love creating apps that can run in a bowser.\n")
