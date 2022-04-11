def palindrome_check(x):
  """checks if given argument is a palindrome
returns "palindrom"(True) or "nie"(False) based on given argument
argument: input by user """
  y = ''.join(reversed(x))
  if y == x:
    return True
  else:
    return False

print("Wpisz słowo:")
x = input()
result = palindrome_check(x)
if result:
  print(f"słowo {x} jest palndromem")
else:
  print(f"słowo {x} nie jest palindromem")

palindrome_check(x)

