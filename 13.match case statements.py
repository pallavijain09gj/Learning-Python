#we don't have match case in this python version 

num = int(input("num: "))

match num:
    case 1:
        print("one")
    case 2:
        print("two") 
    case 3:
        print("three")  
    case _:
        print("other number")     



num = int(input("Enter a number: "))

match num:
    case 0:
        print("Zero")
    case 1 | 2 | 3:
        print("A small positive number")
    case n if n < 0:
        print(f"{n} is negative")
    case n if n % 5 == 0:
        print(f"{n} is positive and divisible by 5")
    case n if n % 2 == 0:
        print(f"{n} is positive and even")
    case n:
        print(f"{n} is positive and odd")

