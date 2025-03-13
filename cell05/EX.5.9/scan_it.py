import sys
import re

def scan_text(keyword, text):
  """
  Counts the number of occurrences of a keyword in a string.

  Args:
    keyword: The keyword to search for.
    text: The string to search in.

  Returns:
    The number of occurrences of the keyword, or None if the number of parameters is incorrect or the keyword is not found.
  """
  if len(sys.argv) != 3:
    return None
  else:
    matches = re.findall(keyword, text)
    if matches:
      return len(matches)
    else:
      return None

if __name__ == "__main__":
  if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    result = scan_text(keyword, text)
    if result is None:
      print("none")
    else:
      print(result)
  else:
    print("none")