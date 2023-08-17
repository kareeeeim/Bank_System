class User:
    def __init__(self , Fname ,Lname, age,address,phone) :
        self.Fname=Fname
        self.Lname=Lname
        self.age=age
        self.address=address
        self.phone=phone
class Bank(User):
    total_deposit=0
    total_withdraws=0
    def __init__(self, Fname,Lname,age,address,phone,balance):
        super().__init__(Fname,Lname,age,address,phone)       
        self.balance=balance
    def show_Info(self):
        return f" dear {self.Fname}\nyour age is :{self.age}\nyour Address is :{self.address}\nyour phone is :{self.phone}\nyour balance =E {round(self.balance,2)}"
    def deposit(self):
        dp=float(input(f"{self.name.title()},Plz enter How much would u like to Deposit = " ))  
        print('Thank U for depositing....')
        self.balance+=dp
        self.total_deposit+=1
        return f"Your balance now is = {round(self.balance,2)}"
    def withdraws(self):
        wd=float(input(f"{self.name.title()},Plz enter How much would u like to Withdraw = " ))
        if wd>self.balance:
            print("U can't Withdraw that amount")
        else :
            print('Thank U for Withdrawing')
            self.balance-=wd
            self.total_withdraws+=1 
            return f"{self.name.title()}, your balance now = {round(self.balance,2)}"
def Options(User_2):    
    while True:
        opt_choice=int(input('\nChoice Your Operation\n1- See Balance\n2- Withdraw\n3- Deposit\n4- Total Withdraw\n5- Total Deposit\n6- Quit\n:'))
        if opt_choice==1:
           print(user_1_bank.show_Info) 
           if opt_choice==1 and User_2 !=None:
            print(user_1_bank.show_Info())
        elif opt_choice==2:
            ww=input(f'{User_1.name} would U like to Withdraw (Yes - No)\n: ')
            if ww.lower() == 'Yes' :
                print(user_1_bank.withdraws()) 
            if ww.lower()=='No':print(Options(User_2));        
        elif opt_choice ==3:
            dd=input(f'{User_1.name} would U like to Deposit (Yes - No)\n:' )
            if dd.lower()=='Yes':
                    print(user_1_bank.deposit())
            if dd.lower()=='No':
                    print(Options(User_2))        
        elif opt_choice==4:
            if opt_choice==4 and User_2 !=None:
                 print(f"There Have been {user_1_bank.total_withdraws} Withdraws")
                 
        elif opt_choice==5:
            if opt_choice==5 and User_2 !=None:
             print(f"There Have been {user_1_bank.total_deposit} Deposit")
        elif opt_choice==6:
            print('Thank U For Using E Bank')
            return False
            break;
def Bank_creation(Fname):
    balance=float(input(f"{Fname.title()} ,how much money U have?\n= "))
    return balance
                 
while True:
        print('Welcome in E Bank')
        Fname=input('Plz enter your First name : ')
        Lname=input('Plz enter your Last  name : ')
        age=int(input('Enter your age : '))
        address=input("Plz enter Your Address : ")
        phone=input('Plz enter Your Phone : ')  
        User_1=User(Fname,Lname,age,address,phone)
        User_2=None
        new_user=input("if U want to create a new account Type 'Yes'\n:")
        if new_user.lower()=='Yes':
            Fname=input('Plz enter your First name : ')
            Lname=input('Plz enter your Last  name : ')
            age=int(input('Enter your age : '))
            address=input("Plz enter Your Address : ")
            phone=input('Plz enter Your Phone : ')  
            User_2=User(Fname,Lname,age,address,phone)
            print('Thank U for registration ')
            user_1_balance=Bank_creation(User_1.Fname)
            user_2_balance=Bank_creation(User_2.Fname)
            user_1_bank=Bank(User_1.Fname,User_1.age,user_1_balance)
            user_2_bank=Bank(User_2.Fname,User_2.age,user_2_balance)
            flag=Options(User_2)       
            if flag == False: break;
        else:
            user_1_balance=Bank_creation(User_1.Fname)
            user_1_bank=Bank(User_1.Fname,User_1.Lname,User_1.age,User_1.address,User_1.phone,user_1_balance)
            flag=Options(User_1)    
            if flag == False : break;
                  