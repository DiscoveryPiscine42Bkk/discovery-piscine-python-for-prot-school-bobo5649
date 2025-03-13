def play_with_arrays():
    """สร้างและจัดการอาร์เรย์ตัวเลข"""

    # สร้างอาร์เรย์ต้นฉบับ
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]

    # สร้างอาร์เรย์ใหม่โดยการเพิ่ม 2 เข้ากับแต่ละค่า
    new_array = [num + 2 for num in original_array]

    # แสดงอาร์เรย์ทั้งสอง
    print("Original array:", original_array)
    print("New array:", new_array)

if __name__ == "__main__":
    play_with_arrays()