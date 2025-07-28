num = int(input("enter a number:  "))

if num>50:
    print("number is greater than 50")
    if num%2==0:
        print("and it is even")
    else:
        print("and it is odd")

else:
    print("number is less than 50")