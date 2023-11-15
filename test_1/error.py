# 捕捉零除异常
# try:
#   print(5 / 0)
# except ZeroDivisionError:
#   print("You can't divide by zero!!")

filename = "./files/test.txt"
try:
  with open(filename) as file_object:
    contents = file_object.read()
except FileNotFoundError:
  pass
  msg = "Sorry, the file " + filename + " does not exist"
  print(msg)


def count_words(file_name: str):
  try:
    with open(file_name) as file_obj:
      contests = file_obj.read()
  except FileNotFoundError:
    m = "Sorry, the file " + file_name + " does not exist"
    print(m)
  else:
    words = contests.split()
    num_words = len(words)
    print("The file " + file_name + " has about " + str(num_words) + "words.")


filename = "alice.txt"
count_words(filename)
