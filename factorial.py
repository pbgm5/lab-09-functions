userstring = input("Number Please ")
usernum = int(userstring)

def factorial(n):
    userinput = 1
    for i in range(1, usernum + 1):
        userinput *= i
print(factorial(usernum))
