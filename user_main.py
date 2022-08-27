from user_functions import Userfunctions
from admin_login import Admin_login

class Usermain:
    def __init__(self,user_obj,admin_obj):
        self.user_obj=user_obj
        self.admin_function_obj=admin_obj
    def Userchoice(self,choice):
        if choice==1:
            self.user_obj.user_registration()
        
        elif choice==2:
            self.user_obj.login()

        elif choice==3:
            self.admin_function_obj.admin_login()
        else:
            print("Incorrect choice")

if __name__=="__main__":
    user_obj=Userfunctions()
    admin_obj=Admin_login()
    main_obj=Usermain(user_obj,admin_obj)
    print(f"*^*^*^*^*^*^*^*^*^EATZZ*^*^*^*^*^*^*^*^*^*\n")
    print(f"____  Welcome To Food ordering APP  ____\n")
    print("!!**********************************************************************")
    print(f"Hello and Welcome \nWhat do you want to do?")
    print("***********************************************************************!!\n")
    while True:
        choice=int(input("1. User Registration\n2. Login User\n3. Admin\n0. To stop\n"))
        if choice==0:
            break
        else:
            main_obj.Userchoice(choice)
