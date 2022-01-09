import os


class vUser:
    def __init__(self, path):
        self.path = path

    def run(self):
        string = "python3 " + self.path
        os.system(string)


dir_path = os.path.dirname(os.path.realpath(__file__))

# run tests
for i in range(1, 7):
    test = vUser(dir_path + "/admin%d.py" % i)
    test.run()
