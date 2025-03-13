def up_low():
    """
    รับสตริงจากผู้ใช้และสลับตัวพิมพ์ใหญ่เป็นตัวพิมพ์เล็ก และในทางกลับกัน
    """
    try:
        input_string = input("ป้อนสตริง: ")  # รับอินพุตจากผู้ใช้
    except EOFError:
        input_string = ""  # กำหนดสตริงว่างเปล่าหากไม่มีอินพุต

    output_string = ""

    for char in input_string:
        if char.isupper():
            output_string += char.lower()
        elif char.islower():
            output_string += char.upper()
        else:
            output_string += char  # คงอักขระที่ไม่ใช่ตัวอักษรไว้ตามเดิม

    print(output_string)  # แสดงผลลัพธ์

if __name__ == "__main__":
    up_low()