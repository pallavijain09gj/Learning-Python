#while loop coditions:  > initialize a variable (before loop)
#                       > write a condition (after while )
#                       > update the variable (inside the loop)
#function : a named block of code you can use again and again
#what is modules? : it is a collection of particular functions (like forming the box)

name = input("enter your name: ")
print("Let's find your percentage")

kan = int(input("enter your kannada marks: "))
while  kan < 0 or kan > 100:  
    kan = int(input("Invalid! enter again: "))



eng = int(input("enter your english marks: "))
while eng < 0 or eng > 100: 
   eng = int(input("Invalid! enter again: "))


    
math = int(input("enter your maths marks: "))
while math < 0 or math > 100: 
    math = int(input("Invalid! enter again: "))


    
phy = int(input("enter your physics marks: "))
while phy < 0 or phy > 100:  
   phy = int(input("Invalid! enter again: "))


    
chem = int(input("enter your chemistry marks: "))
while chem < 0 or chem > 100:   
    chem = int(input("Invalid! enter again: "))


    
comp = int(input("enter your computer marks: "))
while comp < 0 or comp > 100: 
    comp = int(input("Invalid! enter again: "))
    

max_total = 600
total_marks = kan + eng + math + phy + chem + comp
# print("total marks = ",total_marks)
percentage = (total_marks/max_total)*100
# print("your percentage is =",percentage,"%")

if percentage >= 90:
    Grade = "A+"
elif percentage >= 80:
    Grade = "A"
elif percentage >= 70:
    Grade = "B"
elif percentage >= 60:
    Grade = "C"
else :
    Grade = "D" 

print(f"{'Name':<12}: {name}")
print(f"{'total':<12}: {total_marks}")
print(f"{'percentage':<12}: {percentage}")
print(f"{'Grade':<12}; {Grade}")
# 'and' = both conditions must be true
# 'or' = at least one conditions must be true 