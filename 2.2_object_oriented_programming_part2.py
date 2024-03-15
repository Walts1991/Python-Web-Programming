class Program():   #This defines the class, not the function
    def __init__(self, *args, **kwargs):     #The init method is special and gets called when we create a new object of this class
        self.lang = input("What language?: ")
        self.version = float(input("What version?: "))
        self.skill = input("What skill level?: ")
        
    def upgrade(self):
        new_version = float(input("What version?: "))
        print("We have updated the version for", self.lang, "to", new_version)
        self.version = new_version
        
p1 = Program()
#p2 = Program()

print(p1)
print(p1.lang)
print(p1.version)
#print(p2)
#print(p2.lang)
#print(p2.version)

p1.upgrade()

print(p1)
print(p1.lang)
print(p1.version)