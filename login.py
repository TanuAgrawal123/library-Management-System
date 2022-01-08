import csv


class Login():
    name=""
    password=""

    def signupuser(self, username, password, repassword):
        flag=False
        with open('usersignupdetails.csv','r') as readercsv:
            if (password!=repassword):
                print("password didn't match")
                return False
            else:
                csvreader=csv.reader(readercsv)
                for row in csvreader:
                    if (row[0]==username):
                        print("username already exist")
                        return False
        readercsv.close()
        with open('usersignupdetails.csv', 'a', newline="") as appendcsv:
            writecsv=csv.writer(appendcsv)
            list=[username,password]
            writecsv.writerow(list)
        appendcsv.close()
        self.name=username
        self.password=password

        return True

    def getusername(self):
        return self.name

    def loginverification(self,username, password):
        with open('usersignupdetails.csv','r') as readcsv:
            csvreader=csv.reader(readcsv)
            for row in csvreader:
                if(row[0]==username and row[1]==password):
                    return True
        readcsv.close()
        return False