import os


class vUser:
    def __init__(self, path):
        self.path = path

    def run_user(self):
        string = "python " + self.path
        os.system(string)


dir_path = os.path.dirname(os.path.realpath(__file__))

# Login tests
test1 = vUser(dir_path + "/no_answer_submit.py")
#test2 = vUser(dir_path + "/change_last_name.py")
#test3 = vUser(dir_path + "/change_email_address.py")

# List of virtual user tests
Users = []

# Add all tests to list
Users.append(test1)
#Users.append(test2)
#Users.append(test3)

# Run tests
for i in Users:
    i.run_user()
