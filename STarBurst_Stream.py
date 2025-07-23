ms = 300
Wp1 = 10
Wp2 = 20
Wp3 = 30
while True:
    Pdicition = input("พิมเลข 1/2 (1 to Continue, 2 to Quit): ")
    
    if Pdicition == "2":
        break
    else:
        print("เผลอเดินเหยีบMonster")
        print("Monster HP: ", ms)

        Times = int(input("กรุณากรอกจำนวนครั้งที่ต้องการตี: "))
        
        for i in range(Times):
            ChoosWp = input("เลือกอาวุธ (Wp1 = 10 Dm, Wp2 = 20 Dm, Wp3 30 Dm): ")
            
            if ChoosWp == "Wp1":
                ms -= Wp1
            elif ChoosWp == "Wp2":
                ms -= Wp2
            elif ChoosWp == "Wp3":
                ms -= Wp3
            else:
                print("อาวุธไม่ถูกต้องควายโง่")
            
            print("Monster HP เหลือ: ", ms)
            
            if ms == 0:
                print("Monster ตายแล้ว")
                break
            elif ms < 0:
                print("Monster HP Reset to Full")
                ms = 300
            if i == Times - 1:
                print("U dead Noob")
                break
