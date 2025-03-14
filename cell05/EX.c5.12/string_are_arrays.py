#!/usr/bin/env python3
import sys

def main():
    # ตรวจสอบว่ามีการส่งพารามิเตอร์มาถูกต้องหรือไม่
    if len(sys.argv) != 2:
        print("none")
        return
    
    input_string = sys.argv[1]
    # นับจำนวนตัวอักษร 'z' ในสตริง (ไม่สนใจตัวพิมพ์ใหญ่/พิมพ์เล็ก)
    z_count = input_string.lower().count('z')
    
    if z_count == 0:
        print("none")
    else:
        print('z' * z_count)

if __name__ == "__main__":
    main()
