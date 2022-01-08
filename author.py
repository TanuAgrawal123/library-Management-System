import csv
import os


class Author():
    name = ""

    book_title = ""
    publish_date = ""
    author_file=""
    def __init__(self):

        self.author_file="C:\\Users\\anubh\\PycharmProjects\\Library_Management_System\\authorfile.csv"
    def author_info(self, authorname):
        flag=False
        with open(self.author_file , 'r') as readcsv:
            csvreader=csv.reader(readcsv)
            for row in csvreader:
                if(row[0]==authorname):
                    flag=True
                    self.name=authorname

                    self.book_title=row[1]
                    self.publish_date=row[2]
                    print("Details")
                    print("author    book_title   publish_date")
                    print(self.name, self.book_title, self.publish_date)
                    print()
                    break
        if(flag==False):
            print("No such author in database")
    def add_author(self, author, bookname, publish_date):
        try:
            with open('authorfile.csv', 'a', newline="") as writecsv:
                print(author)
                csvwriter=csv.writer(writecsv)
                list=[author,bookname,publish_date]
                csvwriter.writerow(list)
            writecsv.close()
        except:
            print("Not found")
    def delete_author(self, author, bookname):
        try:
            flag=False
            with open('authorfile.csv','r') as readcsv:
                csvreader=csv.reader(readcsv)
                try:
                    with open('authorfile_new.csv', 'w', newline="") as writecsv:
                        csvwriter=csv.writer(writecsv)
                        for row in csvreader:
                            if row[0]==author and row[1]==bookname:
                                flag=True
                            else:
                                csvwriter.writerow(row)
                    writecsv.close()
                except Exception as e:
                    print(e)
            readcsv.close()
            if flag==False:
                print("no author found")
            os.rename('authorfile.csv', 'temp.csv')
            os.rename('authorfile_new.csv','authorfile.csv')
            os.remove('temp.csv')
        except Exception as e:
            print(e)






