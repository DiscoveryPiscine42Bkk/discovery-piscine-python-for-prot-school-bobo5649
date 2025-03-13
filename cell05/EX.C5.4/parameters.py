#!/usr/bin/env python3

import sys

def main():
    """แสดงจำนวนพารามิเตอร์ที่ส่งไปยังโปรแกรม"""
    num_params = len(sys.argv) - 1  # ลบ 1 เพราะ sys.argv[0] คือชื่อสคริปต์
    print(f"Number of parameters: {num_params}.")

if __name__ == "__main__":
    main()