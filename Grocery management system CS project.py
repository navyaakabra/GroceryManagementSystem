import mysql.connector
connection=mysql.connector.connect(host='localhost',user='root',passwd='Navyaa@2005',database='grocery')
c=connection.cursor()

def Add_C():
    c_id=input('Enter Customer ID: ')
    name=input('Enter Customer Name: ')
    c_num=int(input('Enter Contact Number: '))
    address=input('Enter Address: ')
    visit=1
    a="insert into customer values('"+str(c_id)+"','"+str(name)+"',"+str(c_num)+",'"+str(address)+"',"+str(visit)+")"
    c.execute(a)
    connection.commit()
    print('Customer Added')

def Update_C():
    c_id=input('Enter Customer ID: ')
    print('\n1.Name','\n2.Contact Number','\n3.Address','\n4.No of Visits')
    choice_4=int(input('Enter Your Choice which has to be Updated: '))
    if choice_4==1:
        name=input('Enter New Name: ')
        c.execute("Update Customer set NAME='"+str(name)+"'where C_ID='"+str(c_id)+"'")
        connection.commit()
        print('\nCustomer Updated')
    elif choice_4==2:
        phn=input('Enter New Contact Number: ')
        c.execute("Update Customer set CONTACT_NUMBER="+str(phn)+" where C_ID='"+str(c_id)+"'")
        connection.commit()
        print('\nCustomer Updated')
    elif choice_4==3:
        address=input('Enter New Address: ')
        c.execute("Update Customer set ADDRESS='"+str(address)+"'where C_ID='"+str(c_id)+"'")
        connection.commit()
        print('\nCustomer Updated')
    elif choice_4==4:
        nov=input('Enter New Number Of Visits: ')
        c.execute("Update Customer set NO_OF_VISITS="+str(nov)+" where C_ID='"+str(c_id)+"'")
        connection.commit()
        print('\nCustomer Updated')

def View_one_C():
    c_id=input('Enter Customer ID: ')
    c.execute("Select * from customer where C_ID='"+str(c_id)+"'")
    for i in c:
        print(i)
    
    

print(' '*30,"="*20)
print(' '*34,'GROCERY STORE MANAGEMENT SYSTEM')
print(' '*30,'='*20)

while True: 
    print("\n1.Login")
    print("2.Exit")
    choice_1=int(input('Enter Your Choice: '))
    if choice_1==1:
        if choice_1==1:
            name=input("\nEnter Username: ")
            password=input("Enter Password: ")
            if name=='1' and password=='1':
                while True:
                    print('\n1.Customer','\n2.Employee','\n3.Stocks','\n4.Billing','\n5.Exit')
                    choice_2=int(input('Enter Your Choice: '))
                    if choice_2==1:
                        print('1.Add a New Customer')
                        print('2.Update Existing Customer')
                        print("3.View One Customer's Details")
                        print("4.View All Customers' Details")
                        choice_3=int(input('Enter Your Choice: '))
                        if choice_3==1:
                            Add_C()
                        elif choice_3==2:
                            Update_C()
                        elif choice_3==3:
                            View_one_C()
                        elif choice_3==4:
                            pass
                            #View_C()
                        else:
                             print('\nWrong Choice Entered\n')
                             pass
                    elif choice_2==2:
                        pass
                    elif choice_2==3:
                        pass
                    elif choice_2==4:
                        pass
                    elif choice_2==5:
                        break
                    else:
                        print('\nWrong Choice Entered\n')
                        pass

                    
            else:
                print("\nWrong Password\n")
    elif choice_1==2:
        break
    else:
        print('\nWrong Choice Entered')