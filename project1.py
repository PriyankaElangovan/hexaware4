class Clerk:
    sal=20000
    desig="Clerk"
    def _init_(self):
        self.uid=input("Enter id: ")
        self.name=input("Enter name: ")
        self.age=input("Enter age : ")
    def display(self):
        print("==============")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age: ",self.age)
        print("Salary: ",self.sal)
        print("Designation: ",self.desig)
    def raiseSal(self):
        print("==============")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age: ",self.age)
        print("Salary: ",self.sal+10000)
        print("Designation: ",self.desig)

class Tester:
    sal=30000
    desig="Tester"
    def _init_(self):
        self.uid=input("Enter id: ")
        self.name=input("Enter name: ")
        self.age=input("Enter age : ")
    def display(self):
        print("==============")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age: ",self.age)
        print("Salary: ",self.sal)
        print("Designation: ",self.desig)
    def raiseSal(self):
        print("==============")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age: ",self.age)
        print("Salary: ",self.sal+20000)
        print("Designation: ",self.desig)

class Developer:
    sal=35000
    desig="Developer"
    def _init_(self):
        self.uid=input("Enter id: ")
        self.name=input("Enter name: ")
        self.age=input("Enter age : ")
    def display(self):
        print("==============")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age: ",self.age)
        print("Salary: ",self.sal)
        print("Designation: ",self.desig)
    def raiseSal(self):
        print("==============")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age: ",self.age)
        print("Salary: ",self.sal+25000)
        print("Designation: ",self.desig)

class Manager:
    sal=40000
    desig="Manager"
    def _init_(self):
        self.uid=input("Enter id: ")
        self.name=input("Enter name: ")
        self.age=input("Enter age : ")
    def display(self):
        print("==============")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age: ",self.age)
        print("Salary: ",self.sal)
        print("Designation: ",self.desig)
    def raiseSal(self):
        print("==============")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age: ",self.age)
        print("Salary: ",self.sal+30000)
        print("Designation: ",self.desig)
  
print("Select any one...")
print("1. Create \n 2. Display \n 3. Raise Salary\n 4. Exit")
ch=int(input("enter your choise: "))
while ch!=4:
    if ch==1:
        print("1. Clerk\n2. Tester\n3. Developer\n4. Manager\n 5. Exit")
        ch2=int(input("Enter your choise: "))
        while ch2!=5:
            if ch2==1:
                c=Clerk()
                break;
            elif ch2==2:
                t=Tester()
                break;
            elif ch2==3:
                d=Developer()
                break;
            elif ch2==4:
                m=Manager()
                break;
    if ch==2:
        c.display()
        t.display()
        d.display()
        m.display()
    if ch==3:
        c.raiseSal()
        t.raiseSal()
        d.raiseSal()
        m.raiseSal()
        
print("Thank you......!")
