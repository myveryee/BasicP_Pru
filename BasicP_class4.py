# def pnt_hello(year):
#     print("Hello from BasicP_class4.py", year)

# pnt_hello(32021)
# pnt_hello("rada")
# pnt_hello(2021.0)
# pnt_hello(True)

# def my_sum(a, b):
#     print("Sum:", a + b)
#     return a + b

# sum_rwi_vava = my_sum(1, 2)
# print("Sum result:", sum_rwi_vava)

# kaw = input(" มีข้าว True/False? ")
# chon = input(" มีช้อน True/False? ")
# def kinkaw(kaw, chon):
#     if kaw == "True" and chon == "True":
#         return "กินข้าวได้"
#     else :
#         return "กินข้าวไม่ได้"
# print(kinkaw(kaw, chon))

# a = int(input("กรอกตัวเลข : "))
# b = int(input("กรอกตัวเลข : "))
# cmd = input("กรอกเครื่องหมาย (+,-) ")
# def calculate(a, b, cmd):
#     if cmd == "+":
#         return a + b
#     elif cmd == "-":
#         return a - b
#     else:
#         return "โง่"
# print(calculate(a, b, cmd))

# box = ["apple", 30, True, "ruler"]
# print(box[0])
# print(box[1]) 
# print(box[3])
# box[0] = "book"
# print(box[0])
# box.append("Pen")
# box.pop(1)
# print(box)
# x = [1, 2, 3,4, 5]
# for i in range(len(x)):
#     print(i , "starterPack")

# for i in x:
#     print(i, "starterPack")

# box_fruit = ["apple", "banana", "cherry"]
# for i in range(len(box_fruit)):
#     if box_fruit[i] == "apple":
#         print("แอปเปิ้ลอร่อย")
#     else:
#         print("not found")

# fruit = ["apple", "banana", "cherry"]
# addFruit = input("Enter fruit: ")
# fruit.append(aFruit)
# def check_fruit(fruit):
#     if fruit == "apple":
#         return "apple aroi"
#     else:
#         return "not found"
# for i in range(len(fruit)):
#     print(check_fruit(fruit[i]))

# students = {
#     "name": "Thanasorn Dusadeeroj" , "age": 19,"ID" : 67130500014
# }
# print(students)
# print(students["name"])
# print(students["age"])
# print(students["ID"])
# students["gender"] = "male"
# print(students)

# me = {"name" : "Phumphuek Jaithaing", "age" : 18, "ID" : 68130500061, }
# if me["age"] >= 18:
#     print("Pass")
# else:
#     print("Not Pass")

# students = [
#     {"name": "Thanasorn Dusadeeroj", "age": 19, "ID": 67130500014},
#     {"name": "Phumphuek Jaithaing", "age": 18, "ID": 68130500061},
#     {"name": "John Doe", "age": 20, "ID": 1234567890}
# ]
# for student in students:
#     print("Name:", student["name"])

# students = [{"name": "Thanasorn Dusadeeroj", "age": 19, "ID": 67130500014},
#             {"name": "satit", "age": 19, "ID": 6713050047}]
# def check_age(students):
#     for student in students:
#         if student["age"] >= 18:
#             student["age"] = "เกิน"
#         else:
#             student["age"] = "ไม่เกิน"
#         return student
    
# print(check_age(student))