import os


class vUser:
    def __init__(self, path):
        self.path = path

    def run_user(self):
        string = "python3 " + self.path
        os.system(string)


dir_path = os.path.dirname(os.path.realpath(__file__))

# Login tests
test1 = vUser(dir_path + "/Managelist1.py")
test2 = vUser(dir_path + "/Managelist2.py")
test3 = vUser(dir_path + "/Managelist3.py")
test4 = vUser(dir_path + "/Managelist4.py")
test5 = vUser(dir_path + "/Managelist5.py")
test6 = vUser(dir_path + "/Managelist6.py")
test7 = vUser(dir_path + "/Managelist7.py")
test8 = vUser(dir_path + "/Managelist8.py")
test9 = vUser(dir_path + "/Managelist9.py")
test10 = vUser(dir_path + "/Managelist10.py")

# List of virtual user tests
Users = []

# Add all tests to list
Users.append(test1)
Users.append(test2)
Users.append(test3)
Users.append(test4)
Users.append(test5)
Users.append(test6)
Users.append(test7)
Users.append(test8)
Users.append(test9)
Users.append(test10)

# Run tests
for i in Users:
    i.run_user()
