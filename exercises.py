#1
# def celcius_to_fahrenheit(cel):
#     f = cel * (9/5) + 32
#     return f

# print(celcius_to_fahrenheit(10))


#2
money={"saving_account":200,"checking_account":100,"under_bed":[500,10,100]}
# print(money["under_bed"][1])

#3
def celcius_to_fahrenheit(cel):
    if cel < -273.15:
        # print('not possible')
        return ""
    else:
        f = cel * (9/5) + 32
        return f

# print(celcius_to_fahrenheit(-273.4))

#4

# temperatures=[10,-20,-289,100]
# for i in temperatures:
#     print(celcius_to_fahrenheit(i))

#5
temps=[10,-20,-289,100]
def tempWriter(temperatures):
    file=open("tempfile.txt",'a')
    for temp in temperatures:
        if temp < -273.15:
            print(temp)
        else:
            strTemp = str(celcius_to_fahrenheit(temp))
            if type(strTemp) != float:
                file.write(strTemp + "\n")
    file.close()

# tempWriter(temps)
#6
import datetime
import glob

def mergeFiles():
    filenames = glob.glob('./Sample-Files/*.txt')
    with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%f") + ".txt",'w') as file:
        for filename in filenames:
            with open(filename,"r") as f:
                file.write(f.read() + "\n")
mergeFiles()
