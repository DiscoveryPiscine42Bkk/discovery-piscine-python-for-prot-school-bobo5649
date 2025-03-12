# รับค่าตัวเลขจากผู้ใช้
num = int(input("Enter a number: "))

# ตรวจสอบเงื่อนไขและแสดงผลลัพธ์
if num < 0:
    print("This number is negative.")
elif num > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")

# เพิ่มโค้ดเพื่อหยุดหน้าจอใน Windows เพื่อให้เห็นผลลัพธ์
input("\nPress Enter to exit...")
