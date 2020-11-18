class Greeting(object):
    def _init_(self):
        self.name=""

    def sayHi(self, name):
        print("Hi, my name is "+name+", which is your name, of course")

    def sayBye(self, name):
        print("Bye, "+name+", wait, is that my name or yours?")

me=Greeting()
name=input("What is your name: ")
me.sayHi(name)
me.sayBye(name)
