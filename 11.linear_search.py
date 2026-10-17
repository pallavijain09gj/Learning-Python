#Write a function that searches for a target value in a list and returns its index

list=[10,13,19,20,35,42,55,68,78,84,99,108]
def linear_search(number):
    for i in range(len(list)):
        if list[i]==number:
            return i       

number=int(input("search number: "))
result=linear_search(number)    
print("index: ",result)