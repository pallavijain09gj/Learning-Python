#break : just exit this loop        #break also in while loop
for i in range(12):
    print("2 X",i,"=",2*i)
    if i == 10:
        break

print("difference")

for i in range(1,12):
    print("2 X",i,"=",2*i)
    if i == 10:
        break

print("difference")

for i in range(1,12):
    print("2 X",i,"=",2*i)
    if i == 10 :
        print("skip the iteration")
        continue



