
class User:
    def __init__(self,fullname,phonenumber,email,address,password):
        self.fullname=fullname
        self.phonenumber=phonenumber
        self.email=email
        self.address=address
        self.password=password

    def __str__(self):
        return f'Full Name:{self.fullname}\nPhone Number:{self.phonenumber}\nEmail:{self.email}\nAddress:{self.address}'
        
    def get_fullname(self):
        return self.fullname

    def set_fullname(self,fullname):
        self.fullname=fullname

    def get_phonenumber(self):
        return self.phonenumber

    def set_phonenumber(self,phonenumber):
        self.phonenumber=phonenumber

    def get_email(self):
        return self.email

    def set_email(self,email):
        self.email=email

    def get_address(self):
        return self.address

    def set_address(self,address):
        self.address=address

    def get_password(self):
        return self.password

    def set_password(self,password):
        self.password=password

    
