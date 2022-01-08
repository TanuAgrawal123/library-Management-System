import csv
import os


class Student():

    student_info_csv="C:\\Users\\anubh\\PycharmProjects\\Library_Management_System\\student_info.csv"
    def __init__(self):
        self.student_username=""

        self.student_name=""
        self.fee=""
        self.address=""
        self.total_books_issued=0
    def addmember(self, username,name,address,month):
        list=[]
        self.student_username=username

        list.append(self.student_username)



        self.student_name=name;
        list.append(self.student_name)
        self.address=address;
        list.append(self.address)
        self.fee=500*month
        list.append(self.fee)
        list.append(self.total_books_issued)

        with open('student_info.csv', 'a', newline="") as append_csv:
            writecsv=csv.writer(append_csv)
            writecsv.writerow(list)
        append_csv.close()



    def getdetails(self):
        print("Detail of student")
        print("sid   ", self.student_username)
        print("Name  ", self.student_name)
        print("Address  ", self.address)
        print("Membership fee  ", self.fee)

    def update_student_record(self, username, issue):
        with open('student_info.csv', 'r') as searchcsv:
            csvreader = csv.reader(searchcsv)
            with open('student_info_new.csv', 'w', newline="") as new_file:
                csvwriter = csv.writer(new_file)

                for row in csvreader:
                    if (row[0] == username):

                        row[4] = int(row[4]) +issue
                    csvwriter.writerow(row)
            new_file.close()
        searchcsv.close()
        os.rename('student_info.csv', 'student_temp.csv')
        os.rename('student_info_new.csv', self.student_info_csv)
        os.remove('student_temp.csv')

    def is_member(self, username):
        with open('student_info.csv', 'r') as readcsv:
            csvreader = csv.reader(readcsv)
            for row in csvreader:
                if row[0] == username:
                    return True



