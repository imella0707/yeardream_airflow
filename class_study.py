class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
   


    def hello(self):
        print(f"Hello~~!! My name is {self.name}")


user_1 = User("김플", 20)
user_2 = User("피카츄", 10)

# user_1.hello()
# user_2.hello()

# print(user_1.name)
# print(user_1.age)

# print(user_2.name)
# print(user_2.age)


temp = [1,2,3,4,5]

print(type(temp))
print(type(user_1))