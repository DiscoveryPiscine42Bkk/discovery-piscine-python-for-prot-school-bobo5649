import sys

def downcase_it(text):
  """
  แปลงข้อความที่กำหนดให้เป็นตัวพิมพ์เล็กและพิมพ์ออก

  Args:
    text: ข้อความที่จะแปลง
  """
  print(text.lower())

if __name__ == "__main__":
  if len(sys.argv) == 2:
    text = sys.argv[1]
    downcase_it(text)
  else:
    print("mosd")