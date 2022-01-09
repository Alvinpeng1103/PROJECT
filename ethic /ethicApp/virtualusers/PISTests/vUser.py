import os


class vUser:
    def __init__(self, path):
        self.path = path

    def run_user(self):
        string = "python3 " + self.path
        os.system(string)


dir_path = os.path.dirname(os.path.realpath(__file__))

# Coversheet tests
# Virtual test for filling the questions in coversheet page
test1 = vUser(dir_path + "/PIS1.py")
# Virtual test for navigation bar to switch between coversheet and ethics questionnaire
test2 = vUser(dir_path + "/PIS2.py")
test3 = vUser(dir_path + "/PIS3.py")
test4 = vUser(dir_path + "/PIS4.py")
test5 = vUser(dir_path + "/PIS5.py")

# List of virtual user tests
Users = []

# Add all tests to list
Users.append(test1)
Users.append(test2)
Users.append(test3)
Users.append(test4)
Users.append(test5)


# Run tests
for i in Users:
    i.run_user()
