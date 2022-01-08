import csv
import os
import datetime as dt

import pandas
import datetime
from datetime import timedelta, date
from student import Student
from author import  Author

Date_req = date.today() + timedelta(days=5)

print(Date_req)
filename = "book_info.csv"


class LIBRARY():
    no_of_book = 0

    def __init__(self):
        self.filename = "book_info.csv"
        self.fields = []
        self.rows = []
        self.no_of_books = 6

    def get_no_of_books(self):


        # reading csv file
        with open(self.filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)

            self.fields = next(csvreader)
            linecount = 1

            for row in csvreader:
                linecount += 1

            self.no_of_books = linecount
            return self.no_of_books

    def display_book(self):

        with open(self.filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print('              '.join(field for field in self.fields), )
                    line_count += 1
                else:
                    for col in row:
                        print(col, end="              ")
                    line_count += 1
                    print()
        print()

        # df = pandas.read_csv(self.filename)
        # print(type(df[df.Name.str.contains("dbms")]))
        #
        # print(df)


filenaewrite = "C:\\Users\\anubh\\Downloads\\BOOK_INFO_new.csv"
import os
import datetime


class BOOK():
    student_info_csv = "C:\\Users\\anubh\\PycharmProjects\\Library_Management_System\\student_info.csv"

    def __init__(self):
        self.book_id = -1
        self.book_name = ""
        self.author = ""

    def issue_book(self, bid, username):
        with open('student_info.csv', 'r') as readercsv:
            readcsv = csv.reader(readercsv)
            flag = False
            for row in readcsv:
                if row[0] == username:
                    flag = True
                    break
        readercsv.close()
        if (flag == False):
            print("please get membership")
            return

        flag = False
        FOUND = False

        with open('book_info.csv', 'r') as searchcsv:
            csvreader = csv.reader(searchcsv)
            with open('book_info_new.csv', 'w', newline='') as new_file:
                csvwriter = csv.writer(new_file)
                count = 0
                for row in csvreader:

                    id = row[0]
                    bname=row[1]
                    if (id == bid):
                        FOUND = True

                        self.book_id = bid
                        self.book_name=bname
                        self.author = row[3]
                        status = row[6]
                        if (status == "Available"):
                            flag = True

                            row[5] = int(row[5]) - 1
                            if (row[5] == 0):
                                row[6] = "UnAvailable"

                        else:
                            print("BOOK IS OUT OF STOCK")
                    csvwriter.writerow(row)

            new_file.close()
        searchcsv.close()

        if (flag == True and FOUND==True):
            print("BOOK IS ISSUED SUCCESSFULLY")
            print("DETAILS")

            print("book id  ", self.book_id)
            print("book name",self.book_name)
            print("author", self.author)

            print("issue date", date.today())
            print()
            with open('issued_book.csv', 'a', newline="") as writecsv:
                csvwriter = csv.writer(writecsv)
                list = []
                list.append(username)
                list.append(bid)
                list.append(self.author)
                list.append(date.today())
                list.append(date.today() + timedelta(days=15))
                list.append("not returned")
                list.append(0)
                csvwriter.writerow(list)
                student = Student()
                student.update_student_record(username, 1)
            writecsv.close()







        elif(FOUND==False):
            print("No such book")
        os.rename('book_info.csv', 'book_temp.csv')
        os.rename('book_info_new.csv', 'book_info.csv')
        os.remove('book_temp.csv')
        # df = pandas.read_csv(filename)

    def return_book(self,username):
        student = Student()
        if student.is_member(username) == False:
            print("Not a member")
            return
        print("enter book id")
        bid = input()
        return_date=date.today()
        # if bid_exist(bid)==False:
        #     print("BOOK ID DOES NOT EXIST")
        #     return

        with open('issued_book.csv','r') as readcsv:
            csvreader=csv.reader(readcsv)
            flag=False
            fine=0
            with open('issued_book_new.csv', 'a', newline="") as writecsv:
                csvwriter=csv.writer(writecsv)
                for row in csvreader:

                    if (username==row[0] and bid==row[1]):
                        if row[5]!="not returned":
                            print("already returned")
                        else:
                            flag=True
                            row[5]=return_date
                            returning_date = dt.datetime.strptime(row[4], "%Y-%m-%d")
                            returning_date = returning_date.date()
                            re=return_date-returning_date

                            if(re.days>0):
                                fine=re.days*50
                                row[6]=fine
                    csvwriter.writerow(row)
            writecsv.close()
        readcsv.close()
        os.rename('issued_book.csv', 'issue_temp.csv')
        os.rename('issued_book_new.csv', 'issued_book.csv')

        os.remove('issue_temp.csv')
        if flag==True:
            student.update_student_record(username,-1)
            print("Returned successfully with fine ", fine)
        else:
            print("no data found")



    def is_available_not(self, book_id):
        with open('book_info.csv', 'r') as readcsv:
            read_csv = csv.reader(readcsv)
            for row in read_csv:
                if (row[0] == book_id):
                    self.book_id = book_id
                    self.book_name = row[1]
                    self.author = row[3]
                    if (row[6] == "Available"):
                        print("Available")
                        return 1
                    else:
                        print("Not Avaialble")
                        return 0
            print("INVALID BOOK_ID")
            return 2

        read_csv.close()

    def add_book(self, bookname, author, price, publish_date, copies):
        library = LIBRARY()
        bid = 100 + library.get_no_of_books()

        library.get_no_of_books()
        try:
            with open('book_info.csv', 'a', newline="") as appendcsv:
                writecsv = csv.writer(appendcsv)

                list = [bid, bookname, price, author, publish_date,  copies, "Available"]
                writecsv.writerow(list)
            appendcsv.close()
            print("book is added successfully with book id =  ", bid)
            authors=Author()
            authors.add_author(author,bookname,publish_date)

        except:
            print("FILE NOT FOUND")

    def delete_book(self, bid):
        try:
            FOUND=False
            with open('book_info.csv', 'r') as searchcsv:
                csvreader = csv.reader(searchcsv)
                with open('book_info_new.csv', 'w', newline="") as new_file:
                    csvwriter = csv.writer(new_file)
                    for row in csvreader:
                        if (bid == row[0]):
                            FOUND = True
                            self.book_name=row[1]
                            self.author=row[3]
                        else:
                            csvwriter.writerow(row)
                new_file.close()
            searchcsv.close()

            if (FOUND==False):
                print("incorrect bookid")
            else:
                print("Deleted successfully")
            os.rename('book_info.csv', 'book_temp.csv')
            os.rename('book_info_new.csv', 'book_info.csv')
            os.remove('book_temp.csv')
            author=Author()
            author.delete_author(self.author,self.book_name)
        except Exception as e:
            print(e)

    def update_book(self, bid, copies):
        try:
            with open('book_info.csv', 'r') as searchcsv:
                csvreader = csv.reader(searchcsv)
                with open('book_info_new.csv', 'a', newline='') as new_file:
                    csvwriter = csv.writer(new_file)
                    for row in csvreader:
                        if (bid == row[0]):
                            FOUND = True
                            row[5]=copies
                            row[6]="Available"


                        csvwriter.writerow(row)
                new_file.close()
            searchcsv.close()

            if (FOUND == False):
                print("incorrect bookid")
            else:
                print("Updated  successfully")


            os.rename('book_info.csv', 'book_temp.csv')
            os.rename('book_info_new.csv', 'book_info.csv')
            os.remove('book_temp.csv')

        except:
            print("FILE NOT FOUND")





