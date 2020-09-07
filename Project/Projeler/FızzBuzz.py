def FizzBuzz(n):
    if n%3==0 and n%5==0:
        return "FizzBuzz"
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    else:
        return str(n)
length=int(input("Length of array:"))

for i in range(1,length):
    print(FizzBuzz(i))