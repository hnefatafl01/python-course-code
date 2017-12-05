import datetime
import time
r"""
    some info ignoring special characters like '\n'
"""
filename=datetime.datetime.now()
lst = [];
def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M") + ".txt","w") as file:
        file.write("Do the things good dude")

# create_file()
"""
using time module
"""

def timer():
    with open(filename.strftime("%Y-%m-%d-%H-%M") + ".txt","w") as file:
        for i in range(5):
            lst.append(datetime.datetime.now())
            time.sleep(2)
        for i in lst:
            print(i)
timer()
