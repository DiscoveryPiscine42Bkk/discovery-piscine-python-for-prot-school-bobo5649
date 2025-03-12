#!/usr/bin/python3

def to25():
    """
    รับค่าตัวเลขจากผู้ใช้ และแสดงตัวเลขตั้งแต่ค่านั้นจนถึง 25
    หากตัวเลขที่รับมามากกว่า 25 จะแสดง "Error"
    """

    try:
        num = int(input("Enter a number less than 25\n"))

        if num > 25:
            print("Error")
            return

        while num <= 25:
            print(f"Inside the loop, my variable is {num}")  # แก้ไขตรงนี้
            num += 1

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    to25()