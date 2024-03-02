##Tey Ye Xiang
##Edwardus

##Tey Ye Xiang login interface 
def who():
    print ("press 0 to login as admin")
    print ("press 1 to login as customer")
    print ("press 2 to terminate the system")
    log_in =input(str("Please enter your option here:"))
    if log_in == "0":
        admin_login_process()
    elif log_in =="1":
        customer_login_process()
    elif log_in=="2":
        print("Thank you , see you again")
        exit()
    else:
        print("Invalid choice, please choose again")
        who()

##Tey Ye Xiang admin login
def admin_login_process():
    username= input("Please enter your username here: ")
    if username == 'admin':
        password= input("Please enter your password here: ")
        if password == 'admin123':
            admin()
        else:
            print('Invalid password')
            admin_login_process()
    else:
        print('Invalid username')
        admin_login_process()


def customer_login_process():
    custid = input("Please enter your username: ")
    custpw = input("Please enter your password: ")
    with open('alldetail.txt.','r')as reader:
        customer_details = reader.readlines()
        for line in customer_details:
            line = line.rstrip()
            newline = line.split(':')
            if newline[5] == custid and newline[6] == custpw:
                print('Login sucessful')
                customer(custid)

##Tey Ye Xiang admin actions            
def admin():
    while True:
        print("\nWelcome admin")
        print("1.\tCreate profile for new customer")
        print("2.\tview customer profile")
        print("3.\tview all transactions of specific customer")
        print("4.\tview all transactions for specific date")
        print("5.\tview deposit transactions for specific date")
        print("6.\tview withdrawal transactions for specific date")
        print("7.\treturn to admin login tab")
        print("8.\treturn to login tab")
        admin_action= int(input("Choose your action here:"))
        if admin_action ==1:
             register()
        elif admin_action==2:
            view_detail()
        elif admin_action==3:
            view_customer_transaction()
        elif admin_action==4:
            view_transaction_date()
        elif admin_action==5:
            view_deposit_date()
        elif admin_action==6:
            view_withdrawal_date()
        elif admin_action==7:
            admin_login_process()
        elif admin_action==8:
            who()
        
##Tey Ye Xiang admin action 6
def register():   
    print("please enter details of new customer below")
    cust_first_name = input("Please enter customer's first name here:")
    cust_last_name = input("Please enter customer's last name here:")
    cust_age=int(input("Please enter customer's age here:"))
    if cust_age < 18:
        print ("customer is underage to register for a bank account\n Registration cancelled\nYou will be returned to previous tab")
        register()
    elif cust_age > 100:
         print ("customer is too old to register for a bank account\n Registration cancelled\nYou will be returned to previous tab")
         register()
    else:
        bal= float(input('Please input the balance in your bank: '))
        cust_IC=input("Please enter customer's IC no(XXXXXX-XX-XXXX) here:")
        last_char=cust_IC[-4:]
        if len(cust_IC)!=14:
            print("IC number is not valid , please try again")
            register()
        else:
            cust_HP=input("Please enter customer's phone number(only malaysian number):+60")
            if len(cust_HP)!=9 and len(cust_HP)!=10:
                print("HP number is not valid , please try again")
                register()
            else:
                cust_username =(cust_first_name+cust_last_name)
                cust_password =(cust_first_name+last_char)
                cust_details=[]
                cust_details.append(cust_first_name)
                cust_details.append(cust_last_name)
                cust_details.append(str(cust_age))
                cust_details.append(cust_IC)
                cust_details.append(str("+60"+cust_HP))
                cust_details.append(cust_username)
                cust_details.append(cust_password)
                cust_details.append(str(bal))
                print("customer profile\nusername :"+cust_username+"\npassword:"+cust_password)
                with open ('alldetail.txt','a') as f:
                    f.write(':'.join(cust_details)+'\n')
                admin()

##Tey Ye Xiang admin action 2
def view_detail():
    rec = []
    print('1 - View  All Customer Details')
    print('2 - View Specific Customer Details')
    admin_detail_opt = int(input('Please enter your option'))
    if admin_detail_opt == 1:
        with open('alldetail.txt.','r')as fh:
            detail=fh.read()
            print('\n'+detail)
            admin()
    elif admin_detail_opt == 2:
        with open('alldetail.txt.','r')as fh:
            for line in fh:
                rec.append(line.strip().split(':'))
        linecount=len(rec)
        user_detail=input('Please enter customer username')
        for clm in range(linecount):
            if user_detail in rec[clm][5]:
                print(rec[clm])
                admin()
            else:
                print("customer not found , please try again")
                view_detail()

def view_customer_transaction():
    cust_id=input('Please enter customer username: ')
    details = []
    with open('transaction.txt','r') as fr:
        for line in fr:
            details.append(line.strip().split(':'))
    linecount = len(details)
    for row in range(linecount):
        if cust_id in details[row][0]:
            print(details[row])

##Tey Ye Xiang admin action 3
def view_transaction_date():
    cus_date=input('Please enter transaction date(dd/mm/yyyy):')
    rec = []
    with open('transaction.txt','r') as fr:
        for line in fr:
            rec.append(line.strip().split(':'))
    linecount = len(rec)
    for row in range(linecount):
        if cus_date in rec[row][1]:
            print(rec[row])

##Tey Ye Xiang admin action 4
def view_deposit_date():
    rec=[]
    cus_date=input('Please enter deposit date: ')
    with open('transaction.txt','r') as fh:
        for line in fh:
            rec.append(line.strip().split(':'))
        linecount=len(rec)
        for row in range(linecount):
            if cus_date in rec[row][1]:
                print(rec[row][2])


##Tey Ye Xiang admin action 5
def view_withdrawal_date():
    rec=[]
    cus_date=input('Please enter deposit date: ')
    with open('transaction.txt','r') as fh:
        for line in fh:
            rec.append(line.strip().split(':'))
        linecount=len(rec)
        for row in range(linecount):
            if cus_date in rec[row][1]:
                print(rec[row][3])

    
def customer(custid):
    print("\nThe followings are all the available services provided:\n1.Deposit\n2.Withdrawal\n3.View own transaction history")
    choice= int(input("Select your choice by inputting the assigned number for each service: "))
    if choice == 1:
        deposit(custid)
    elif choice == 2:
        withdrawal(custid)
    elif choice == 3:
        view(custid)
    else:
        print("Invalid choice. Please select the correct number again.")

def deposit(custid):
    dep_rec=[]
    deposit_amount = float(input('Enter the amount you want to deposit: '))
    date = input('Enter the date you deposit your money(dd/mm/yyyy): ')
    withdraw = '0'
    ##read bal
    with open('alldetail.txt','r') as file:
        detail = file.readlines()
        for line in detail:
            line = line.rstrip()
            new = line.split(':')
            if new[5] == custid:
                balance = float(new[7])
                new_balance= (balance+deposit_amount)
                new[7] = str(new_balance)
                print('Done')
    file.close()
    ##write deposit 
    dep_rec.append(custid)
    dep_rec.append(date)
    dep_rec.append(str(deposit_amount))
    dep_rec.append(withdraw)
    with open('transaction.txt','a') as f:
        f.write(':'.join(dep_rec)+'\n')
    customer(custid)

def withdrawal(custid):
    wit_rec=[]
    withdraw_amount = float(input('Enter the amount you want to withdraw: '))
    date = input('Enter the date you deposit your money(dd/mm/yyyy): ')
    depo = '0'
    ##read bal
    with open('alldetail.txt','r') as file:
        detail = file.readlines()
        for line in detail:
            line = line.rstrip()
            new = line.split(':')
            if new[5] == custid:
                balance = float(new[7])
                new_balance= (balance-withdraw_amount)
                new[7] = str(new_balance)
                print('Done')
    file.close()
    ##write withdraw
    wit_rec.append(custid)
    wit_rec.append(date)
    wit_rec.append(depo)
    wit_rec.append(str(withdraw_amount))
    with open('transaction.txt','a') as f:
        f.write(':'.join(wit_rec)+'\n')
    customer(custid)

def view(custid):
    details = []
    with open('transaction.txt','r') as fr:
        for line in fr:
            details.append(line.strip().split(':'))
    linecount = len(details)
    for row in range(linecount):
        if custid in details[row][0]:
            print(details[row])
        

print("Welcome to HappyBank, nice to meet you")
who()

         
  
           
    
   
       
        
            
    
                  
    



