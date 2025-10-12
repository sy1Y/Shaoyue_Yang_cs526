#Problem1
import os

def is_palindromic(n):
  s = str(n)
  return s == s[::-1]
def process_palindromes():
    if not os.path.exists('input.txt'):
        print("Error：can't find 'input.txt'")
        return
    with open('input.txt', 'r') as file:
      lines = file.readlines()

    strings = [line.strip() for line in lines if line.strip()]
    total_palindrome = 0
    results = []
    for s in strings:
      if is_palindromic(s):
          results.append("true")
          total_palindrome += 1
      else:
          results.append("false")
    for result in results:
        print(result)
    print(total_palindrome)
      
if __name__ == "__main__":
    process_palindromes()
