# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.imp
#import sys
#sys.path.append(".")
from book_info import LIBRARY
from book_info import BOOK
from student import Student
from author import Author
from login import Login
from staff import Staff

def menu(choice):
    if (ch==1 or ch==3):
        print("WELCOME TO READING ROOM OF INDIA")
        print("PRESS 1 TO DISPLAY AVAIALBLE BOOKS")
        print("PRESS 2 TO GET MEMBERSHIP OF LIBRARY AS STUDENT")
        print("PRESS 4 TO RETURN A BOOK")
        print("PRESS 3 TO ISSUE A BOOK")
        print(" PRESS 5 check for particular book avaiablity")
    if(ch==2 or ch==4):
        print("Welcome to Reading book of India")
        print("Press 1 TO DISPLAY AVAIALBLE BOOKS")
        print("PRESS 2 TO GET MEMBERSHIP AS STAFF")
        print("PRESS 3 TO CHECK AUTHOR DETAILS")
        print("PRESS 4 TO ADD_BOOK")
        print("PRESS 5 TO DELETE A BOOK")
        print("press 6 TO UPDATE A BOOK")


if __name__ == '__main__':

    login = Login()
    while(True):
        print("Welcome to Reading book of India")
        print("Press 1 for Signup as student")
        print("press 2 for signup as faculty")
        print("press 3 for login as student")
        print("press 4 for login as faculty")
        ch = int(input())
        if(ch==1 or ch==2):
            print("Enter username")
            name=input()
            print("Enter password")
            password=input()
            print("Renter Password")
            repassword=input()
            result=login.signupuser(name, password,repassword)
            while(result!=True):
                print("Enter username")
                name = input()
                print("Enter password")
                password = input()
                print("Renter Password")
                repassword = input()
                result = login.signupuser(name, password, repassword)
            username=login.getusername()
            break
        elif(ch==3 or ch==4):
            print("Enter username")
            name=input()
            print("enter password")
            password=input()
            result=login.loginverification(name, password)

            if result==True:
                username = name
                break
            print("Incorrect Details")
            print()



    menu(ch)
    flag=False
    while(flag==False):
        try:
            choice=int(input())
            library = LIBRARY()
            flag=True
        except:
            print("enter valid input")


    while (choice!=0):
        if(choice==0):
            print("THANKS FOR CHOOSING US")
            exit(0)
        elif(choice==1):
            library.display_book()
        elif(choice==3 and (ch==1 or ch==3)):
            print("enter book bid")
            bid=input()
            book=BOOK()
            book.issue_book(bid, username)
        elif(choice==5 and (ch==1 or ch==3)):
            book=BOOK()
            print("Enter bookid")
            bid=input()
            book.is_available_not(bid)
        elif(choice==2 and (ch==1 or ch==3)):
            print("Thankyou for choosing us")
            print("Enter your Details")
            print("Enter Name")
            name=input()
            print("Enter address")
            address=input()
            print("Enter months for membership")
            while True:
                try:

                    month=int(input())
                    break
                except ValueError:
                    print("enter valid number")

            student=Student()
            student.addmember(username,name, address, month)
            print("SUCCESSFULLY REGISTERED")
            print("Details are")
            student.getdetails()

        elif(choice==3 and (ch==2 or ch==4)):
            author=Author()
            print("please enter name of the author")
            name=input()
            author.author_info(name)

        elif (choice==4 and (ch==2 or ch==4)):
            print("ADD A BOOK IN LIBRARY")
            staff=Staff()

            staff.add_book(username)
        elif (choice==2 and(ch==2 or ch==4)):
            staff=Staff()
            print("enter name")
            name=input()
            print("enter address")
            address=input()
            staff.add_as_staff(name, address, username)

        elif (choice==5 and(ch==2 or ch==4)):
            staff=Staff()
            staff.deletebook(username)

        elif (choice==6 and(ch==2 or ch==4)):
            staff=Staff()
            staff.updatebook(username)
        elif (choice==4 and (ch==1 or ch==3)):
            book=BOOK()
            book.return_book(username)
        else:
            print("enter coorect choice")



        menu(ch)

        print("PRESS 0 TO QUIT")
        try:
            choice = int(input())
        except e:
            print("Enter valid Integer no")










# See PyCharm help at https://www.jetbrains.com/help/pycharm/
