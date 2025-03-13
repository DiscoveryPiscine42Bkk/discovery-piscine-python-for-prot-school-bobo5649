def remove_duplicates(arr):
  """
  ลบค่าที่ซ้ำกันออกจากอาร์เรย์โดยไม่ลบค่าออกจากอาร์เรย์ต้นฉบับโดยตรง
  """
  seen = set()
  result = []
  for item in arr:
    if item not in seen:
      seen.add(item)
      result.append(item)
  return result

# ตัวอย่างการใช้งาน
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
result_array = remove_duplicates(original_array)

print(original_array)
print(result_array)