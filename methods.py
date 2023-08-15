class Product:
    company_name = "KPMG"
    def __init__(self):
        self.prdid=int(input("Enter the product id:- "))
        self.prdname=input("Enter the product name:- ")
        self.prdquan=int(input("Enter the product quantity:- "))
        self.price = 480

    @classmethod
    def pro_name_cal(cls):
        cls.company_name= "KPMG ltd"

    @staticmethod
    def total_quan_price_cal(q,p):
        qnty_price = q * p
        return qnty_price

    def show(self):
        print("Your Product id is:- ",self.prdid)
        print("Your Product name is:- ",self.prdname)
        print("Your Product quantity is:- ",self.prdquan)
        print("Total Product price is:- ",self.price)
        Total_price = self.total_quan_price_cal(self.prdquan,self.price)
        print("Total_price ::",Total_price)
        print("Product Company name before:- ",Product.company_name)
        self.pro_name_cal()
        print("Product Company name After:- ",Product.company_name)

obj=Product()
obj.show()










