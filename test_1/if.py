car = "BMW"
name = "Ted"


def print_slice():
  print("----------------------------")


if car != "BMW":
  print("is not")
else:
  print("is")

if car == "BMW" and name == "Ted":
  print("is")

cars_log = ["BMW", "BYD", "W", "WenJie", "XiaoPeng"]
cars = ["BMW", "One"]

print_slice()
for car in cars:
  if car in cars_log:
    print("Yes " + "in the Big logs")
  else:
    print("No " + "not in the Big logs")
