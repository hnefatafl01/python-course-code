# greeting = input("Write a greeting: ")
# print(greeting)


# a = 2
# b = 3
# product = a * b
# print(product)




# s = "hello"
# c = ["h",2, "hi"]

#list
# print(type(c))
# print(type(s))

#tuples
# t = ("Hello",3,4,5)
# print(type(t))

#dictionary
# l = [2,3,4]
# d = {"Name":"Kevin", "Surname":"Erickson", "cities": ("billings", "bozeman", "denver")}
# d["Name"]



# def age_foo(age):
#     new_age = int(age) + 50
#     return new_age
#
# age = input("What is your age?: ")
# if int(age) < 150:
#     age_foo(age)
# else:
#     print("how is that possible")


# conditionals
# a = 5
# if a < 5:
#     print("less than 5")
# elif a == 5:
#     print("equal to 5")
# else:
#     print("greater than 5")

#loops
# emails=["me@gmail.com","you@yahoo.com","some@hotmail.com"]
# for item in emails:
#     if 'gmail' in item:
#         print(item)
#
# password=''
# while password != 'python123':
#     password = input("Enter Password: ")
#     if password == 'python123':
#         print('Logged in')
#     else:
#         print('invalid password')
#

names=['james','john','jack']
email_domains=['gmail','hotmail','yahoo']
for i,j in zip(names,email_domains):
    print(i,j)
