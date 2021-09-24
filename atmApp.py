from _typeshed import Self


class Atm (object):
    def __init__(self,cardNumber,pinNumber,):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    def cashWithdrawal(self,amount):
        balance = 50000
        left = balance - amount
        print(left)
    def balanceEnquiry(self):
        print("Your Balance is 50000")
    def desposit(self):
        deposit = input("how much you want to deposit")
        self.balance += deposit
def main():
    cardno = input("insert the card number")        
    pinno = input("insert the pin number")
    carddetails = Atm(cardno,pinno)
    print("Choose your Activity")
    print ("1 : balance enquiry")
    print (" 2 : withdrawal ") 
    activity = int(input(" Enter Acitivity Number"))
    if (activity == 1):
        carddetails.balanceEnquiry()
    elif(activity == 2):
        amount = int(input("Enter ythe withdrawal Amount"))
        carddetails.cashWithdrawal(amount)
    else :
        print("Enter a Valid Number")
if __name__ == "__main__":
    main()
        
