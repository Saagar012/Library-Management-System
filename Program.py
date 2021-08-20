def listSplit():
    global bookname
    global authorname
    global quantity
    global cost
    #initializing an empty list.
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]
    #opening a stockfile to read it.
    with open("stock.txt","r") as f:
        #reading the each lines and put them in a list.
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]#removing \n from each index
        for i in range(len(lines)):
            ind=0
            #spliting the each item of the list which are seperated by comma and put each of them line by line.
            for a in lines[i].split(','):
                #print(a)
                #appending on bookname[] if the user enters  0.
                if(ind==0):
                    bookname.append(a)
                #appending on authorname[] if the user enters 1.
                elif(ind==1):
                    authorname.append(a)
                #appending on quantity[] if the user enters 2.
                elif(ind==2):
                    quantity.append(a)
                #appending on cost[] if the user enters 3.
                elif(ind==3):
                    cost.append(a)
                #increasing the 'ind' by 1 everytime
                ind+=1

#Declaring a borrowBook function,every code related to borrowing book is coded inside it.
def borrowBook():
    name=input("Enter the name of the borrower: ")
    #Using try except method as the user name can't be the integer or float. 
    try:
        name=int(name)
        print(" Enter a valid name!!")
        borrowBook()
    except:
        try:
            name=float(name)
            print(" Enter a valid name!!")
            borrowBook()
        except:
            print("Valid borrower name !!")  
    #storing the input name on 't' variable.   
    t="Borrow-"+name+".txt"
    #writing some information to create an invoice after borrowing the books.
    with open(t,"w+") as f:#opening the 't' file to write some information in it.
        f.write("=========================================================================\n")
        f.write("\t\tLibrary Management System \n")   
        f.write("\t\t\tof \n\t\tInformatics College Pokhara\n")
        f.write("=========================================================================\n")
        f.write("               Borrower's Name:- "+ name+"\n\n")
        f.write("    Date: " + getDate()+"          Time:"+ getTime()+"     Address: Ranipauwa-Pokhara\n")
        f.write("\t\t\t\t\t\t PhoneNo: 061-56278\n")
        f.write("_________________________________________________________________________\n")
        f.write("S.N. \t:\tBookname \t\t    :      Authorname \n" )
        f.write("_________________________________________________________________________\n")
    print("Please select an option below:")
    try:    #using a for loop whose indexing starts from 0 and continues upto 1 less than the totallength of the book.
        for i in range(len(bookname)):
            print("Enter", i, "to borrow book", bookname[i])
        #storing the user input number in 'a' variable.
        a=int(input())
        if(int(quantity[a])>0):
            print("Book is available and it is borrowed!!")
            print("The no. of books borrowed is: 1 " )
            #opening 't' file and appending the below information on it.
            with open(t,"a") as f:
                f.write("1. \t:\t%-28s:     %s"%( bookname[a],authorname[a])+"\n")
            #decreasing the quantity of books by 1 from stock file.
            quantity[a]=int(quantity[a])-1
            #opening the stock file and writing the updated quantity of books in the stockfile.
            with open("Stock.txt","w+") as f:
                for i in range(3):
                    f.write(bookname[i]+","+authorname[i]+","+str(quantity[i])+","+cost[i]+"\n")
        
            #multiple book borrowing code
            for j in range(2):
                print("Do you want to borrow next book?")
                print("Press Y for Yes")
                choice=input()
                #changing the input 'y' into uppercase.
                if(choice.upper()=="Y"):
                    print("Please select a option below:")
                    for i in range(len(bookname)):
                        print("Enter", i, "to borrow book", bookname[i])
                    a=int(input())
                    with open(t,"r") as f:
                        data=f.read()
                    if bookname[a] in data:
                        print("You have already Borrowed that book!!")
                        borrowBook()
                    else:
                        if(int(quantity[a])>0):
                            print("Book is available and it is borrowed!!")
                            print("The no. of books borrowed is:- " +str(j+2) )
                            with open(t,"a") as f:
                                f.write(str(j+2) +". \t:\t%-28s:     %s"%(bookname[a],authorname[a])+"\n")
                            quantity[a]=int(quantity[a])-1
                            #opening the stockfile and writing the updated quantity of books after multipleborrowing in the stockfile.
                            with open("Stock.txt","w+") as f:
                                for i in range(3):
                                    f.write(bookname[i]+","+authorname[i]+","+str(quantity[i])+","+cost[i]+"\n")
                else:
                    break 
               
        else:
            print("Book is not available")
            
        with open(t,"a") as f:
                f.write("=========================================================================")
    except:
        print("Please enter the valid no. to borrow  particular book")
        borrowBook()







def getDate():
        #importing date
        from datetime import date
        today = date.today()
        #using strftime method to get the date so that we can change the date format as per our wish.
        d2 = today.strftime("%b/%d/%Y")
        #print("Burrowed date - ", d2)
        #returning our output date so that it can be used in other functions.
        return d2

def getTime():
        from datetime import datetime
        now = datetime.now()
        #using strftime method to get the time. 
        time = now.strftime("%H:%M:%S")
        #print("Burrowed Time  - ",time)
      #returning the time so we can give access to other functions.
        return time 




#Declaring the returnBook function.
def returnBook():
    name=input("Enter name of borrower: ")
    #Storing the input name file in 'a' variable.
    a="Borrow-"+name+".txt"
    #error handling which means evenif the user inputs a wrong keyword,program doesn't stops.
    #if the user enters a correct input,code inside the try runs.
    try:
        with open(a,"r") as f:
            data=f.read()
            print(data)
    #incase if the user inputs a wrong keyword,code inside the except runs.
    except:
        print("The borrower name is incorrect")
        returnBook()
    
    #writing suitable information to create an invoice after returning the books.
    b="Return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("==========================================================================\n")
        f.write("\t\tLibrary Management System \n")   
        f.write("\t\t\tof \n\t\tInformatics College Pokhara\n")
        f.write("==========================================================================\n")
        f.write("               Returned By:- "+ name+"\n\n")
        f.write("    Date: " + getDate()+"          Time:"+ getTime()+"     Address: Ranipauwa-Pokhara\n")
        f.write("\t\t\t\t\t\t PhoneNo: 061-56278\n")
        f.write("__________________________________________________________________________\n")
        f.write("S.N.\t:\tBookname\t\t\t : Cost\t\n"  )
        f.write("__________________________________________________________________________\n")
          
    total=0.0
    for i in range(3):
        #looks whether the book is borrowed or not.
        if bookname[i] in data:
            #opening the 'b'file and appending the below information.
            with open(b,"a") as f:
                f.write(str(i+1)+"\t:\t"+"%-33s:%s"%(bookname[i],cost[i])+"\n")
                quantity[i]=int(quantity[i])+1
            total+=float(cost[i])
    with open(b,"a") as f:
        f.write("==========================================================================\n")


        
    print(total)
    #ask the user whether the book return date is expired or not.
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat=input()
    #changing the user input small y into uppercase sothat the program doesn't show much error.
    if(stat.upper()=="Y"):
        print("By how many days was the book returned late?")
        day=int(input())
        print("How many books were borrowed?")
        books=int(input())
        if (books>3):
            print ("Please enter the valid no. of books that the borrower had borrowed!!")
            returnBook()
        elif (books<1):
            print ("Please enter the valid no. of books that the borrower had borrowed!!")
            returnBook()
        else:
            fine=2*day*books
            with open(b,"a")as f:
                f.write("\t\t\t\t\t\t Fine: $"+ str(fine)+"\n")
            total=total+fine
            print("Final Total", total)
            with open(b,"a")as f:
                f.write("\t\t\t\t\t\t Total: $"+ str(total))
            #opening the stock file and writing all the information with the updated quantity of books in it. 
            with open("Stock.txt","w+") as f:
                    for i in range(3):
                        f.write(bookname[i]+","+authorname[i]+","+str(quantity[i])+","+cost[i]+"\n")
    elif(stat.upper()=="N"):
        print("Final Total", total)
        with open(b,"a")as f:
            f.write("\t\t\t\t\t\tTotal: $"+ str(total))
        #opening the stock file and writing all the information with the updated quantity of books in it. 
        with open("Stock.txt","w+") as f:
                for i in range(3):
                    f.write(bookname[i]+","+authorname[i]+","+str(quantity[i])+","+cost[i]+"\n")
    else:
        print("You entered a wrong keyword!!"+"Try again and press Y or N")
        returnBook()
    


#Declaring the start function which is the first funtion to run in our program.
def start():
    #error handling,Here if the user inputs the correct keyword,code inside the try runs.
    try:    #while true is used for never ending loop                                                                         
        while(True):
            print("=====================================================  ")
            print("           Welcome to the library management system!!  ")
            print("=====================================================  ")
            print("Enter 1. To Display the Stock details")
            print("Enter 2. To Borrow a book")
            print("Enter 3. To return a book")
            print("Enter 4. To exit")
            a=int(input("Select a choice from 1-4: "))
            if(a==1):
                #Opening the stock file to read it.
                with open("stock.txt","r")as f:
                    #reads each line of stock file and puts them in a list with\n at the end in each index.
                    lines=f.readlines()
                    lines=[x.strip('\n') for x in lines]#removing \n from each index
                    print(lines)
            elif(a==2):#listSplit function is called first sothat it is easier to access the book's name,quantity,cost in burrowBook function.
                listSplit()
                borrowBook()
            elif(a==3):#listSplit function is called first sothat it is easier to access the book's name,quantity,cost in returnBook function.
                listSplit()
                returnBook()
            elif(a==4):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
    #if the user inputs the wrong keyword program doesn't stops and runs the code inside the except.
    except:
        print("Please enter a valid choice from 1-4")
        start()
#Calling the start function.
start()


