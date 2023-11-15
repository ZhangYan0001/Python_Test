from collections import OrderedDict

import cv2
import matplotlib.pyplot as plt


class Dog:

  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age
    self.host_name = ""

  def sit(self):
    print(self.name.title() + "is now sitting.")

  def roll_over(self):
    print(self.name.title() + "rolled over")

  def set_host_name(self, name: str):
    self.host_name = name

  def get_info(self):
    print("the dog name is " + self.name.title(), "and its age is", self.age,
          "its host_name is " + self.host_name)

  def growth(self, ages: int):
    self.age += ages


my_dog = Dog("hello", 10)
my_dog.set_host_name("my")
my_dog.get_info()
my_dog.growth(2)
my_dog.get_info()


class KeKeDog(Dog):

  def __init__(self, name: str, age: int, color: str, sex: bool):
    super().__init__(name, age)
    self.color = color
    self.sex = sex


my_KeKeDog = KeKeDog("world", 13, "yellow", True)

names = OrderedDict()

names["Jen"] = "python"
names["Sarah"] = "c"
names["phil"] = "ruby"
names["Ale"] = "Java"

print(names)
