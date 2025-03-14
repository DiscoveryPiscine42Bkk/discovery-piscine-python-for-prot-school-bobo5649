#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์หรือไม่
if len(sys.argv) == 1:
    print("7")
else:
    print(f"parameters: {len(sys.argv) - 1}")
    # ใช้ for loop เพื่อแสดงผลพารามิเตอร์และความยาวของแต่ละพารามิเตอร์
    for arg in sys.argv[1:]:
        print(f"{arg}: {len(arg)}")
