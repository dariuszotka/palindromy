#pierwsza metoda
print("Wpisz słowo:")
x = input()
def palindrome_check(x):
  """checks if given argument is a palindrome
returns "palindrom"(True) or "nie"(False) based on given argument
argument: input by user """
  y = ''.join(reversed(x))
  while y == x:
    True
    print("palidrom")
    break
  while y != x:
    False
    print("nie")
    break
  
palindrome_check(x)

help(palindrome_check)

#druga metoda


print("Wpisz słowo:")
x = input()
def palindrome_check(x):
  """checks if given argument is a palindrome
returns "palindrom"(True) or "nie"(False) based on given argument
argument: input by user """
  y = ''.join(reversed(x))
  if y == x:
    print("palindrom")
  else:
    print("nie")

palindrome_check(x)

help(palindrome_check)