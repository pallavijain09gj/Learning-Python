student = {"name":"Pallavi","age":18,"kcet rank":32000}
print(student)
print(type(student))    
student["kcet rank"] = 32579
print(student)
student["city"]="Bangalore"
print(student)
student["colloge"]="cambridge institute of technology"
print(student)
del student['age']
print(student)
if "age" in student:
    print("age is available")
for key in student:
    print(key)
for value in student.values():
    print(value)    
for key, value in student.items():
    print(key," = " ,value)    