contacts=dict()
print("1. ADD CONTACT:")
print("2. EDIT CONTACT:")
print("3. VIEW CONTACT:")
print("4. DELETE CONTACT:")
print("5. EXIT:")
choice=0
while choice<5:
    try:
        choice=int(input("enter your choice:"))
        if choice==1:
            name=input("enter the name:")
            phone=input("enter the phone number:")
            contacts[name]=phone
            
            for x,y in contacts.items():
                print(x,y)
        elif choice==2:
            print("1. change name")
            print("2. change number")
            choice=int(input("enter your choice:"))
            if choice==1:
                old_name=input("enter the old_name:")
                if old_name in contacts:
                    new_name=input("enter the new_name:")
                    contacts[new_name]=contacts[old_name]
                    contacts.pop(old_name)
                    
                    print("contact edited successfully")
                else:
                    print("contact not found")
            elif choice==2:
                old_name=input("enter the old_name:")
                if old_name in contacts:
                    new_number=int(input("enter the new_number:"))
                    contacts[name]=new_number
                    print("contact edited successfully")
                else:
                    print("contact not found")
        elif choice==3:
            for x,y in contacts.items():
                print(x,y)
        elif choice==4:
            del contacts["manu"]
            print(contacts)
        elif choice==5:
            print(exit)
            break
    except:
        print("invalid")
            

            
        




