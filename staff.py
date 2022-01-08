import csv
from book_info import BOOK

class Staff():
    username=""
    name = ""
    address = ""


    def add_as_staff(self, name, address, username):
        try:
            with open('staff.csv', 'a', newline="") as appenddcsv:
                csvwriter = csv.writer(appenddcsv)
                list = [username, name, address]
                csvwriter.writerow(list)
            appenddcsv.close()
            self.username=username
            self.name=name
            self.address=address
        except:
            print("FILE NOT FOUND")
    def is_staff(self, username):
        try:
            with open('staff.csv','r') as readcsv:
                csvreader=csv.reader(readcsv)
                for row in csvreader:
                    if row[0]==username:
                        return True
            readcsv.close()
            return False
        except:
            print("FILE NOT FOUND")

    def add_book(self,username):
        if self.is_staff(username)==False:
            print("Not register as staff account cann't add book")
            return
        print("Enter book name")
        name=input()
        print("Enter author")
        author=input()
        print("Enter publish date format(dd/mm/yy)")
        pdate=input()
        print("Enter price per book")
        price=input()
        print("enter copies of book")
        copies=input()

        book=BOOK()
        book.add_book(name,author,price, pdate, copies)

    def deletebook(self, username):
        if self.is_staff(username)==False:
            print("Not register as staff cann't delete book")
            return
        print("Enter book id")
        bid=input()
        book = BOOK()
        book.delete_book(bid)
    def updatebook(self, username):
        if self.is_staff(username)==False:
            print("Not register as stadd cann't update book")
            return
        print("Enter book id")
        bid=input()
        print("ENTER COPIES OF BOOK")
        copies=input()
        book=BOOK()
        book.update_book(bid,copies)








