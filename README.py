class vehicle():
    def __init__(self,speed,name):
        self.name=name
        self.speed=speed
        print("The speed of car:",self.speed)
        print("The name of car is:",self.name)
class BMW(vehicle):
    def __init__(self,speed,name,model):
        self.model=model
        print("Model:",self.model)
        vehicle.__init__(self,speed,name)
obj1=BMW(200,"BMW","X5 model")







class person():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print("Employee name:",self.name)
        print("Employee id:",self.id)
class employee(person):
    def __init__(self,name,id,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,id)
obj1=employee("Rahul",123,20000,"intern")
obj1.display()
print("Salary:",obj1.salary)
print("Post",obj1.post)
obj2=employee("Rohit",113,35000,"manager")
obj2.display()
print("Salary:",obj2.salary)
print("Post",obj2.post)
