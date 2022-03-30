print("Wpisz słowo:")
x = input()
def palindrome_check(x):
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


print("Wpisz słowo:")
x = input()
def palindrome_check(x):
  y = ''.join(reversed(x))
  if y == x:
    print("palindrom")
  else:
    print("nie")

palindrome_check(x)

help(x)