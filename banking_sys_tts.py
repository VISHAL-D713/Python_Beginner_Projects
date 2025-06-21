import pyttsx3 as py
xx = py.init()
xx.say('Hellow')
xx.runAndWait()
def speek(text):
    xx.say(text)
    xx.runAndWait()
class Bank_Accound():
    def _init_(self,balance,acc):
        self.balance=balance
        self.acc=acc
        data = f'Your ACC Balance is {self.balance} and \nyour acc no is {self.acc}'
        print(data)
        speek(f'Your ACC Balance is {self.balance} and your acc no is {self.acc} ')
        f= open('vn.txt','a')
        f.write(data)
        f.close()

    def debit(self,amount):
        self.amount=amount
        self.balance+=amount
        data = f"\nRS {self.amount} was debited on this accound no {self.acc} and \nyour available balance is {self.balance}"
        print(data)
        speek(f"RS {self.amount} was debited on this accound no {self.acc} and your available balance is {self.balance}  ")
        f= open('vn.txt','a')
        f.write(data)
        f.close()

    def credit(self,amount):
        self.amount=amount
        self.balance-=amount
        data = f"\nRS {self.amount} was cridit on this acoound no {self.acc} and \nyour available balance is {self.balance}"
        print(data)
        speek(f"\nRS {self.amount} was cridit on this acoound no {self.acc} and your available balance is {self.balance}  ")
        f= open('vn.txt','a')
        f.write(data)
        f.close()
speek('Enter your Accound Balance')
AB = int(input("Enter your Accound Balance"))
speek('Enter your Accound Number')
AN = int(input("Enter your Accound Number"))
speek('Enter Amount to credit')
CDT = int(input("Enter Amount to credit "))
speek('Enter Amount to Debit')
DBT = int(input("Enter Amount to Debit "))
f= open('vn.txt','a')
f.write('\n\nNew Acc Detail \n')
f.close()
c1 = Bank_Accound(AB,AN)
c1.credit(CDT)
c1.debit(DBT)