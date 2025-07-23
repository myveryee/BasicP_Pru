distance = int(input("กรุณากรอกระยะทาง: "))
if 5 <= distance <= 50:
    price = 10
elif 51 <= distance <= 100:
    price = 15
elif 101 <= distance <= 300:
    price = 25
elif 301 <= distance <= 500:
    price = 35
elif distance > 500:
    price = 45
else:
    price = 0
    print("กุไม่ส่งของให้มึงหรอก")

if price > 0:
    print("ค่าส่งสำหรับระยะทาง" ,distance ,"คือ" ,price ,"บาท")
 
# userdicition = str(input("ส่งไหม Yes/No: "))
# if userdicition.lower() == "yes":
#     distance = int(input("กรุณากรอกระยะทาง: "))
#     if distance >= 5:
#         price = 10
#         if distance > 50:
#             price = 15
#             if distance > 100:
#                 price = 25
#                 if distance > 300:
#                     price = 35
#                     if distance > 500:
#                         price = 45
#         print(f"ค่าส่งสำหรับระยะทาง {distance} คือ {price} บาท")                  
#     else:
#         price = 0
#         print("กุไม่ส่งของให้มึงหรอก")
# else:
#     print("ไปส่งกะพ่อมึงเองดิ")
