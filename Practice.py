class sistec:
    company_name="Capegemini"
    def __init__(self):
        self.id=int(input("Please enter your id:- "))
        self.name=input("Please enter your name:- ")
        self.sal=int(input("Please enter your sal:- "))

    def show(self):
        print("Welcome to the brand",sistec.company_name)
        print("Id is",self.id)
        print("Name is ",self.name)
        print("Salary is ",self.sal)
        bonus=self.bonus_cal(self.sal)
        print("*"*25)
        print("Total sal before bonus ",self.sal)
        print("Total sal after bonus ",self.sal+bonus)
        print("*"*25)


    def bonus_cal(self,sal):
        b=self.sal * 10/100
        return b

obj=sistec()
obj.show()


