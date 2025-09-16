class Bank():

    bank_name:str
    person_name:str
    account_no:int
    balance:int

    def set_bank(self,bank_name,person_name,account_no,balance):

        self.bank_name=bank_name
        self.person_name=person_name
        self.account_no=account_no
        self.balance=balance

    def deposit(self,amount):

        self.balance+=amount

    def withdraw(self,amount):

        if self.balance<amount:
            print("insuffient balance")
        else:
            self.balance-=amount
        print("withdrawed",amount)
    
    def balance(self):
        print(f"ur balance is ")

    def display_bank(self):

        print(self.bank_name,self.person_name,self.account_no,self.balance)


bank_instance=Bank()

bank_instance.set_bank("SBI","Akash",123456789,1000)
bank_instance.balance()
