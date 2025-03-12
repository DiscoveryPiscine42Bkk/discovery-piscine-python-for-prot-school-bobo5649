def multiplication_table():
    """สร้างตารางสูตรคูณตามจำนวนที่ผู้ใช้ป้อน"""

    try:
        number = int(input("ป้อนตัวเลข: "))
        for i in range(1, 10):
           print(f"{i} x {number} = {i * number}")
    except ValueError:
        print("กรุณาป้อนตัวเลขจำนวนเต็ม")

if __name__ == "__main__":
    multiplication_table()