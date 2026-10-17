
import time

date = time.strftime("%d/%m/%Y", time.localtime())
print(date)
t = time.strftime("%H:%M:%S", time.localtime())
print(t)
hour = int(time.strftime("%H"))
print(hour)


if (hour>0 and hour<12):
    print("Good Morning")
elif (hour>=12 and hour<16):
    print("Good Afternoon") 
elif (hour>=16 and hour<20):
    print("Good Evening")
else:
    print("Good Night")