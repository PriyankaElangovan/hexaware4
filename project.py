class Clerk :
    salary=15000;
    desig="CLERK";
    
    def __init__(self) :
        self.uid=input("Enter ID :");
        self.name=input("Enter NAme :");
        self.age=input("Enter Age  :");
    
    def display(self):
        print("Emp Deteils ........!");
        print("Name :",self.name);
        print("ID : ",self.uid);
        print('Age :',self.age);
        print('Salary ',self.salary);
        print('Desig :',self.desig);
        
    def raiseSal(self):
        print("Agter Raising the salary .....!");
        print("Name :",self.name);
        print("ID : ",self.uid);
        print('Age :',self.age);
        print('Salary ',self.salary+20000);
        print('Desig :',self.desig);

        print("select any one:")
        print("1.Create \n 2.Display \n 3.Raise Salary \n 4.Exit")
        ch=int(intput("enter your choice:")
        while ch!=4;
                   if ch==1:
                       print("1.Clerk \n 2.Tester \n 3.Develpoer \n 4. Manager")
                       ch2=int(intput("Enter your choice:")
                               while ch2!=5:
                                   ch=int(intput("enter your choice: "))
                                   while ch!=4:
                                       if ch==1:
                                           print("1.clerk \n 2.Tester \n 3.developer \n 4.manager\n")
                                           ch2=int(input("Enter your choice: "))
                                           while ch2!=5;
                                           if ch2==1:
                                               c=clerk()
                                               elif ch2==2:
                                                   t= Tester()
                                                   elif ch2==3:
                                                       d=Developer()
                                                       elif ch2==4:
                                                           m=manager()
                                                           if ch==2:
                                                               c.display()
                                                               elif ch2==3:
                                                                   d=Developer()
                                                                   elif ch2==4:
                                                                       m=Manager()
                                                                       if ch==2:
                                                                           c.display()
                                                                           t.display()
                                                                           d.display()
                                                                           m.display()
                                                                           if ch==3:
                                                                               c.raisesal()
                                                                               t.raiseSal()
                                                                               d.raiseSal()
                                                                               m.raisesal()
                                                                               print("thank you!!")
                                            
                                        
                                        
                        
