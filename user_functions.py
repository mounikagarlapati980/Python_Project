from user_details import User
from admin_functions import Admin_functions
import re

class Userfunctions:
    user_dict={}
    def __init__(self):
        self.order_list=[]

    def user_registration(self):
        fullname=input("Enter Full Name: ")
        phonenumber=input("Enter 10 digits Phone Number: ")
        while not(re.findall('^[0-9]{10}$',phonenumber)):
            print('Incorrect format')
            phonenumber=input("Enter Phone Number: ")
        email=input('Enter email: ')
        while not(re.findall(r"[a-zA-Z0-9._]+[@]+[a-z]+[.]+[a-z]+$",email)):
            print('Incorrect format')
            email=input('Enter email: ')
        address=input("Enter Address: ")
        password=input('Enter Password: ')
        Userfunctions.user_dict[email]=User(fullname,phonenumber,email,address,password)
        print("User registered successfully")

    def login(self):
        username=input("Enter Username: ")
        password=input("Enter Password: ")
        try:
            if Userfunctions.user_dict[username].password ==password:
                print("Login Successful")
                while True:
                        choice=int(input(("Enter your Choice:\n1. Place Order\n2. Order History\n3. Update Profile\n0. To go back\n")))
                        if choice==1:
                            self.place_order()
                        elif choice==2:
                            self.order_history()
                        elif choice==3:
                            self.update_profile(username)
                        elif choice==0:
                            break
                        else:
                            print("Incorrect choice")
            else:
                print("Password is wrong")

        except KeyError:
            print("Username not found")


    def place_order(self):
        self.adminfunc_obj= Admin_functions()
        if len(Admin_functions.admin_dic):
            self.adminfunc_obj.viewfood_item()
            lst=list(map(int,input().split()))
            cost=0
            for i in lst:
                try:
                    if Admin_functions.admin_dic[i].stock>=Admin_functions.admin_dic[i].quantity:
                        self.order_list.append(Admin_functions.admin_dic[i])
                        Admin_functions.admin_dic[i].stock-=Admin_functions.admin_dic[i].quantity
                        print('Your order is placed')
                        sellprice=Admin_functions.admin_dic[i].price-(Admin_functions.admin_dic[i].discount*Admin_functions.admin_dic[i].price)/100
                        cost=cost+sellprice
                        print(f'ID:{Admin_functions.admin_dic[i].id}\tName:{Admin_functions.admin_dic[i].name}\tQuantity:{Admin_functions.admin_dic[i].quantity}\tPrice:{Admin_functions.admin_dic[i].price}\tDiscount:{Admin_functions.admin_dic[i].discount}\tCost:{sellprice}')
                    else:
                        print("Insufficient Stock")
                except KeyError:
                    print("Incorrect Id")
            print(f'Total cost:{cost}')
        else:
            print("No items available")

    def order_history(self):
        if len(self.order_list):
            for i in self.order_list:
                sellprice=i.price-(i.discount*i.price)/100
                print(f'Id:{i.id}\tPrice:{i.name}\tQuantity:{i.quantity}\tPrice:{i.price}\tDiscount:{i.discount}\tCost:{sellprice}')
        else:
            print("No Order History")

    def update_profile(self,username):
        while True:
            choice=int(input('Enter your choice:\n1. Update Full Name\n2. Update Phone Number\n3. Update Address\n4. Update Password\n0. To go back\n'))
            if choice==1:
                fullname=input("Enter Full Name: ")
                Userfunctions.user_dict[username].set_fullname(fullname)
                print("updated successfully")
                print(Userfunctions.user_dict[username])
            elif choice == 2:
                phonenumber=(input("Enter 10 digits Phone Number: "))
                while not(re.findall('^[0-9]{10}$',phonenumber)):
                    print('Incorrect format')
                    phonenumber=input("Enter Phone Number: ")
                Userfunctions.user_dict[username].set_phonenumber(phonenumber)
                print("updated successfully")
                print(Userfunctions.user_dict[username])
                
            elif choice == 3:
                address=input("Enter Address: ")
                Userfunctions.user_dict[username].set_address(address)
                print("updated successfully")
                print(Userfunctions.user_dict[username])
            elif choice == 4:
                password=input("Enter Password: ")
                Userfunctions.user_dict[username].set_password(password)
                print("updated successfully")
                print(Userfunctions.user_dict[username])
            elif choice==0:
                break
            else:
                print("Incorrect choice")


