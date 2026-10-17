marks = [45,78,92,33,67,89]
count = 0
total = 0
for i in marks:         #for: takes each item from list, one by one
    if i >= 60:
        total +=i
        count +=1
        print("the numbers are: ", i)
print("the number of marks greater than or equal to 60 are: ",count)
print("total:",total)
avg = total/count
print("average: ",avg)

def calculate_average(marks):   #average of numbers >= 60 marks
    total = 0
    count = 0
    for i in marks:
        if i >= 60:
            total += i
            count += 1
    avg = total/count        
    return total,count,avg    

print(calculate_average(marks))      

def average_of_total(marks):    #average of total marks
    total = 0
    count = 0 
    for i in marks:
        total +=i
        count +=1
    avg = total/count
    return total, count, avg    

print(average_of_total(marks))    

def find_highest(marks):        #to find highest number in the marks list    
    highest = 0         
    for i in marks:
        if i > highest:
            highest = i
    return highest

print(find_highest(marks))

