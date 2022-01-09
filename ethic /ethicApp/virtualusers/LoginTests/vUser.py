import os


class vUser:
    def __init__(self, path):
        self.path = path

    def run(self):
        string = "python3 " + self.path
        os.system(string)


dir_path = os.path.dirname(os.path.realpath(__file__))

# Login tests
test1 = vUser(dir_path + "/login1.py")
test2 = vUser(dir_path + "/login2.py")
test3 = vUser(dir_path + "/login3.py")
test4 = vUser(dir_path + "/login4.py")

# List of virtual user tests
Users = []

# Add all tests to list
Users.append(test1)
Users.append(test2)
Users.append(test3)
Users.append(test4)

# Run tests
for i in Users:
    i.run()
