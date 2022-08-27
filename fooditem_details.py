class Fooditem:
    def __init__(self,id,name,quantity,price,discount,stock):
        self.id=id
        self.name=name
        self.quantity=quantity
        self.price=price
        self.discount=discount
        self.stock=stock

    def __str__(self):
        return f'Id:{self.id}\tName:{self.name}\tQuantity:{self.quantity}\tPrice:{self.price}\tDiscount:{self.discount}\tStock:{self.stock}'

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name=name

    def get_quantity(self):
        return self.quantity

    def set_quantity(self,quantity):
        self.quantity=quantity

    def get_price(self):
        return self.price
    
    def set_price(self,price):
        self.price=price
    
    def get_discount(self):
        return self.discount

    def set_discount(self,discount):
        self.discount=discount

    def get_stock(self):
        return self.stock

    def set_stock(self,stock):
        self.stock=stock