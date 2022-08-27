from admin_functions import Admin_functions
class Admin_login:
    adminfunct_obj=Admin_functions()
    def __init__(self):
        self.username='admin'
        self.password='admin@123'

    def admin_login(self):
        username=input("Enter Username: ")
        password=input("Enter Password: ")
        if self.username==username and self.password==password:
            print("Admin Login Sucessfull")
            while True:
                    choice=int(input("1. Add food item\n2. Edit food item\n3. View food items\n4. remove food items\n0. To go back\n"))
                    if choice==1:
                        Admin_login.adminfunct_obj.addfood_item()
                    elif choice==2:
                        Admin_login.adminfunct_obj.editfood_item()
                    elif choice==3:
                        Admin_login.adminfunct_obj.viewfood_item()
                    elif choice==4:
                        Admin_login.adminfunct_obj.removefood_item()
                    elif choice==0:
                        break
                    else:
                        print("Incorrect choice")
        else:
            print("Invalid Credentials")
