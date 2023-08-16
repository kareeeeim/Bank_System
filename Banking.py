class User:
    def __init__(self , name , age,email,phone) :
        self.name=name
        self.age=age
        self.email=email
        self.phone=phone
class Bank(User):
    total_deposit=0
    total_withdraws=0
    def __init__(self, name, age,email,phone,balance):
        super().__init__(name, age,email,phone)       
        self.balance=balance
    def show_Info(self):
        return f" dear MR|MIS {self.name}\n your email is :{self.email}\n your phone is :{self.phone}\nhas a remaining balance of E {round(self.balance,2)}"
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
        opt_choice=int(input('\nChoice Your Operation\n1- See Balance\n2- Withdraw\n3- Deposit\n4- Total Withdraw\n5- Total Deposit\n6- Quit\n'))
        if opt_choice==1:
           print(user_1_bank.show_Info) 
           if opt_choice==1 and User_2 !=None:
            print(user_1_bank.show_Info())
        elif opt_choice==2:
            ww=input(f'{User_1.name} would U like to Withdraw (Yes - No)\n: ')
            if ww.lower() == 'Yes' :
                print(user_1_bank.withdraws())
            if opt_choice==2 and User_2 !=None:
                print(user_1_bank.withdraws())
        elif opt_choice ==3:
            dd=input(f'{User_1.name} would U like to Deposit (Yes - No)\n:' )
            if dd.lower()=='Yes':
                    print(user_1_bank.deposit())
            if opt_choice==3 and User_2 !=None:
                   print(user_1_bank.deposit())                           
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
        else:
            print('Plz choose any no. from 1 : 6')
def Bank_creation(name):
    balance=float(input(f"{name.title()} ,how much money U have?\n= "))
    return balance
                 
while True:
        print('Welcome in E Bank')
        name=input('Plz enter your name : ')
        age=int(input('Enter your age : '))
        email=input("Plz enter Your Email : ")
        phone=input('Plz enter Your Phone : ')  
        User_1=User(name,age,email,phone)
        User_2=None
        new_user=input("if U want to create a new account Type 'Yes'\n:")
        if new_user.lower()=='Yes':
            name=input('Plz enter your name : ')
            age=int(input('Enter your age : '))
            email=input("Plz enter Your Email : ")
            phone=input('Plz enter Your Phone : ')  
            User_2=User(name,age,email,phone)
            print('Thank U for registration ')
            user_1_balance=Bank_creation(User_1.name)
            user_2_balance=Bank_creation(User_2.name)
            user_1_bank=Bank(User_1.name,User_1.age,user_1_balance)
            user_2_bank=Bank(User_2.name,User_2.age,user_2_balance)
            flag=Options(User_2)       
            if flag == False: break;
        else:
            user_1_balance=Bank_creation(User_1.name)
            user_1_bank=Bank(User_1.name,User_1.age,User_1.email,User_1.phone,user_1_balance)
            flag=Options(User_1)    
            if flag == False : break;
                  