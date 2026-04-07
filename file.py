f = open("demo.txt")
print(f.read())



with open("demo.txt", "w") as f:
  # print(f.readline())
  f.write("Hello this is overwrite")


# name="sachin"
# print(f"my name is {name}. im from nepal ")

class myclass:
  name="sachin"
  age=20

  def printage():
    print("my age is 20")

# myobj=myclass()

# myobj.printage()

print(myclass.name)