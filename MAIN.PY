class myclass:
    __privateVar=21;
    def __privateMethod(self):
        print("I am inside myclass")
    def hello(self):
        print("Private variable value:",myclass.__privateVar)
foo=myclass()
foo.hello()
foo.__privateMethod()  
