def factorial(n):

  total = 1
  for i in range(0, n, 1):
      total = total * (n - i)
      print("Current i is " + i)
      print("The current value of total is " + total)

    return total

userstring = input("Number Please")
usernum = int(userstring)
print(factorial(usernum))
