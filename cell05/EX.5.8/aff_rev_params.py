#!/usr/bin/python3
import sys

def aff_rev_params():
    """
    แสดงสตริงที่ส่งเป็นพารามิเตอร์ในลำดับย้อนกลับ

    หากมีพารามิเตอร์น้อยกว่าสองตัว จะแสดง "none"
    """

    args = sys.argv[1:]  # รับพารามิเตอร์ทั้งหมด ยกเว้นชื่อสคริปต์

    if len(args) < 2:
        print("none")
    else:
        for arg in reversed(args):
            print(arg)

if __name__ == "__main__":
    aff_rev_params()