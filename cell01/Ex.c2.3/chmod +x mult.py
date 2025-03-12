#!/usr/bin/env python3

def main():
    """
    โปรแกรมนี้จะขอให้ผู้ใช้ป้อนตัวเลขสองตัว
    จากนั้นจะแสดงผลคูณของตัวเลขทั้งสอง
    และระบุว่าผลลัพธ์เป็นบวก ลบ หรือศูนย์
    """

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    product = num1 * num2

    if product > 0:
        print("The result is positive.")
    elif product < 0:
        print("The result is negative.")
    else:
        print("The result is zero.")

    print(f"{num1} x {num2} = {product}")


if __name__ == "__main__":
    main()