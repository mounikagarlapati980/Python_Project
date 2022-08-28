from fooditem_details import Fooditem

class Admin_functions:
    admin_dic={}
    id=1

    def addfood_item(self):
        try:
            name=input("Enter Name: ")
            quantity=int(input('Enter Quantity in values: '))
            price=float(input('Enter Price in rupees: '))
            discount=float(input("Enter discount percentage: "))
            stock=int(input("Enter Stock in values: "))
            Admin_functions.admin_dic[Admin_functions.id]=Fooditem(Admin_functions.id,name,quantity,price,discount,stock)
            print('Added new item successfully')
            Admin_functions.id+=1
        except ValueError:
            print("Please try again. Incorrect format!")

    def editfood_item(self):
        if len(Admin_functions.admin_dic):
            try:
                id=int(input("Enter Id which you want to edit: "))
                if id in Admin_functions.admin_dic.keys():
                    choice=int(input("1. Update Food Name\n2. Update Quantity\n3. Update Price\n4. Update Discount\n5. Update Stock \n"))
                    if choice ==1:
                        Admin_functions.admin_dic[id].set_name(input("Enter name: "))
                        print("Updated successfully")
                    elif choice==2:
                        Admin_functions.admin_dic[id].set_quantity(int(input("Enter Quantity in values: ")))
                        print("Updated successfully")
                    elif choice==3:
                        Admin_functions.admin_dic[id].set_price(float(input("Enter Price in rupees: ")))
                        print("Updated successfully")
                    elif choice==4:
                        Admin_functions.admin_dic[id].set_discount(float(input("Enter discount percentage: ")))
                        print("Updated successfully")
                    elif choice==5:
                        Admin_functions.admin_dic[id].set_stock(int(input("Enter Stock in values:")))
                        print("Updated successfully")
                    else:
                        print("Incorrect choice")
                else:
                    print("Food Id is not available!")
            except ValueError:
                print("Please try again. Incorrect format!")
        else:
            print("No items available")


    def viewfood_item(self):
        if len(Admin_functions.admin_dic):
            for i in Admin_functions.admin_dic.values():
                print(i)
        else:
            print("No items available")

    def removefood_item(self):
        if len(Admin_functions.admin_dic):
            id=int(input("Enter Id which you want to delete: "))
            try:
                del Admin_functions.admin_dic[id]
                print("!!Deleted food item successfully!!")
            except KeyError:
                print("Food id not available")
        else:
            print("No items available to remove")